from mountequist import behaviors, responses


def test_bare_minimum_response():
    result = responses.HttpIs().as_dict()

    assert "is" in result
    assert "statusCode" in result["is"]
    assert result["is"]["statusCode"] == 200


def test_full_response():
    result = responses.HttpIs(
        status_code=201,
        headers={"test": "test"},
        body={"body_test": "body_test"},
        mode="NoMode",
        behaviors=behaviors.Wait(500)).as_dict()

    assert "is" in result
    assert "statusCode" in result["is"]
    assert "headers" in result["is"]
    assert "body" in result["is"]
    assert "_mode" in result["is"]
    assert "_behaviors" in result
    assert result["is"]["statusCode"] == 201
    assert result["is"]["headers"] == {"test": "test"}
    assert result["is"]["body"] == {"body_test": "body_test"}
    assert result["is"]["_mode"] == "NoMode"
    assert result["_behaviors"] == {"wait": 500}

