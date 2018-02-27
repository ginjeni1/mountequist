from mountequist import servers, impostors, responses, stubs, clients

if __name__ == '__main__':
    path = "C:\work\mountebank-v1.13.0-win-x64"
    with servers.WindowsServer(path) as server:
        impostor = impostors.Http(stubs.Stub(responses.HttpIs(body="All Ok")))
        client = clients.Http("http://localhost", impostor)
        with client:
            result = client.post_to_impostor(impostor)
            print result
