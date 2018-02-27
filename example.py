from mountequist import clients, impostors, predicates, responses, servers, stubs


if __name__ == '__main__':
    impostor = impostors.Http(
        stubs.Stub(
            responses=responses.HttpIs(body="Easy Reply"),
            predicates=predicates.Equal({"method": "POST", "body": "hmm"})))

    with servers.WindowsServer("C:\\temp\\mountebank-v1.13.0-win-x64"):
        with clients.Http("http://localhost", impostor) as client:
            result_1 = client.post_to_impostor(impostor, data="hmm")
            print(result_1.text)
