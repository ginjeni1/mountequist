from mountequist import predicates


def test_equal_predicate():
    result = predicates.Equal({"body": "Nope"}).as_dict()

    assert "equals" in result
    assert "body" in result["equals"]
    assert "Nope" in result["equals"]["body"]


def test_exists_predicate():
    result = predicates.Exists({"body": "Nope"}).as_dict()

    assert "exists" in result
    assert "body" in result["exists"]
    assert "Nope" in result["exists"]["body"]


def test_and_predicate():
    result = predicates.And(
        predicates.Equal({"body": "Nope"}),
        predicates.Equal({"headers": {"api-key": "yes"}})).as_dict()

    assert "and" in result
    assert "equals" in result["and"][0]
    assert "body" in result["and"][0]["equals"]
    assert "equals" in result["and"][1]
    assert "headers" in result["and"][1]["equals"]


def test_or_predicate():
    result = predicates.Or(
        predicates.Equal({"body": "Nope"}),
        predicates.Equal({"headers": {"api-key": "yes"}})).as_dict()

    assert "or" in result
    assert "equals" in result["or"][0]
    assert "body" in result["or"][0]["equals"]
    assert "equals" in result["or"][1]
    assert "headers" in result["or"][1]["equals"]


def test_not_predicate():
    result = predicates.Not(predicates.Equal({"body": "Nope"})).as_dict()

    assert "not" in result
    assert "equals" in result["not"]
    assert "Nope" in result["not"]["equals"]["body"]
