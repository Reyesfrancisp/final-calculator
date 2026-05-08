import pytest
import uuid
from playwright.sync_api import Page, expect

@pytest.fixture
def auth_user(page: Page, fastapi_server: str):
    """Registers and logs in a unique user for E2E BREAD testing."""
    username = f"test_{uuid.uuid4().hex[:8]}"
    
    # Register
    page.goto(f"{fastapi_server}register")
    page.fill("#first_name", "Test")
    page.fill("#last_name", "User")
    page.fill("#username", username)
    page.fill("#email", f"{username}@example.com")
    page.fill("#password", "SecurePass123!")
    page.fill("#confirm_password", "SecurePass123!")
    page.click("button[type='submit']")
    
    page.wait_for_url("**/login**")

    # Login
    page.fill("#username", username)
    page.fill("#password", "SecurePass123!")
    page.click("button[type='submit']")
    
    page.wait_for_url("**/dashboard**")
    
    return page

def test_add_and_browse_calculation_positive(auth_user: Page, fastapi_server: str):
    """Test Add (POST) and Browse (GET) operations"""
    page = auth_user
    
    # Add a calculation
    page.select_option("#calcType", "addition")
    page.fill("#calcInputs", "5, 10, 15")
    page.click("#calculationForm button[type='submit']")
    
    # Verify Success Message
    expect(page.locator("#successAlert")).to_be_visible()
    expect(page.locator("#successMessage")).to_contain_text("Calculation complete: 30")
    
    # Verify it appears in the Browse list
    table = page.locator("#calculationsTable")
    expect(table).to_contain_text("addition")
    expect(table).to_contain_text("5, 10, 15")
    expect(table).to_contain_text("30")

def test_add_calculation_negative_invalid_input(auth_user: Page, fastapi_server: str):
    """Test Add (POST) negative scenario: insufficient inputs"""
    page = auth_user
    
    # Try to calculate with only one number
    page.select_option("#calcType", "addition")
    page.fill("#calcInputs", "5")
    page.click("#calculationForm button[type='submit']")
    
    # Verify Client-side/Server-side Error
    expect(page.locator("#errorAlert")).to_be_visible()
    expect(page.locator("#errorMessage")).to_contain_text("two valid numbers")

def test_read_and_edit_calculation(auth_user: Page, fastapi_server: str):
    """Test Read (GET ID) and Edit (PUT) operations"""
    page = auth_user
    
    # Create a calculation to edit
    page.select_option("#calcType", "multiplication")
    page.fill("#calcInputs", "2, 3")
    page.click("#calculationForm button[type='submit']")
    expect(page.locator("#calculationsTable")).to_contain_text("6")

    # Read: Click 'Edit' which loads the specific calculation by ID
    page.click("text=Edit")
    page.wait_for_url("**/dashboard/edit/**")
    
    # Edit: Change inputs and Save
    page.fill("#calcInputs", "4, 5")
    page.click("button:has-text('Save Changes')")

    # Verify Success - The Edit page uses window.showToast which renders in #toastContainer
    expect(page.locator("#toastContainer")).to_contain_text("successfully")
    
    # Go back to dashboard and verify the table updated
    page.goto(f"{fastapi_server}dashboard")
    expect(page.locator("#calculationsTable")).to_contain_text("20")

def test_delete_calculation(auth_user: Page, fastapi_server: str):
    """Test Delete (DELETE) operation"""
    page = auth_user
    
    # Create a calculation to delete
    page.select_option("#calcType", "subtraction")
    page.fill("#calcInputs", "10, 4")
    page.click("#calculationForm button[type='submit']")
    expect(page.locator("#calculationsTable")).to_contain_text("6")

    # Handle the browser confirm dialog automatically by accepting it
    page.once("dialog", lambda dialog: dialog.accept())

    # Click Delete
    page.click("button:has-text('Delete')")
    
    # Verify deletion success - The Dashboard uses the static successAlert, NOT the toast!
    expect(page.locator("#successAlert")).to_be_visible()
    expect(page.locator("#successMessage")).to_contain_text("deleted successfully")