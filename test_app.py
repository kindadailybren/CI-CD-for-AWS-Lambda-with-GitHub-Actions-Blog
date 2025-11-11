import app
import json


def test_simple_lambda_handler():
    # Call the handler
    event = {}
    context = {}
    response = app.lambda_handler(event, context)

    # Check the response
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert "Hello dev.to article!" in body["message"]


# We run the test function directly
test_simple_lambda_handler()

print("All tests passed!")
