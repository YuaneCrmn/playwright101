from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="module")
def myIds():
    keys = []
    yield keys

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    request_context.dispose()
    
def test_post_todo(api_request_context: APIRequestContext, myIds) -> None:
    data = { 
        "completed": False,
        "title": "test222",
        "id": "500222",
    }
    new_todo = api_request_context.post(
        "/todos", data=data
    )
    
    assert new_todo.ok
    
    todo_response = new_todo.json()
    
    print("")
    print(f"New Todo request: {new_todo}")
    print(f"todo_response Ver: {todo_response}")
    
    myIds.append(todo_response['id'])

def test_get_todo(api_request_context: APIRequestContext, myIds) -> None:
    get_todo = api_request_context.get(
        f"/todos/{myIds[0]}"
    )
    assert get_todo.ok

    response = get_todo.json()

    assert response['title'] == "test222"
    assert response['completed'] == False

    print(f"Get todo request: {get_todo}")
    print(f"Response: {response}")
