from mountequist import clients, impostors, stubs, responses, predicates


if __name__ == '__main__':
    impostor = impostors.Http(
        stubs.Stub(
            responses=responses.HttpIs(body="OP Stuff"),
            predicates=predicates.Equal({"method": "POST", "body": "hmm"})
        ),
        stubs.Stub(responses=responses.HttpIs(body="Interesting Stuff")))

    client = clients.Http(
        base_url="http://localhost",
        port=2525,
        impostors=[impostor])

    with client:
        result_1 = client.post_to_impostor(impostor, data="hmm")
        print result_1.text
