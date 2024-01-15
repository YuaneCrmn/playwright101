from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    request_context.dispose()
    
def test_post_todo(api_request_context: APIRequestContext) -> None:
    data = { 
        "completed": False,
        "title": "test",
        "id": "500",
    }
    new_todo = api_request_context.post(
        "/todos", data=data
    )
    
    assert new_todo.ok
    
    todo_response = new_todo.json()
    
    print("")
    print(f"New Todo request: {new_todo}")
    print(f"todo_response Ver: {todo_response}")
        