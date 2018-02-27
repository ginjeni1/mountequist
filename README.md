# Mountequist
Used to handle mountebank in contexts of automatic testing.

Compatible with Python 2.7.14+  and Python 3.6+

Currently only supports Windows.


## Examples

You can install and start a mountebank server using
the 'with' statement.
```python
from mountequist import servers

path = "C:\mountebank-v1.13.0-win-x64"
with servers.WindowsServer(path) as server:
    pass
```
If it finds an existing installation it will use it, otherwise
it will download, extract and start it.

You can also use a client to handle the creation of impostors and predicates
```python
from mountequist import clients, impostors, predicates, responses, servers, stubs


impostor = impostors.Http(
    stubs.Stub(
        responses=responses.HttpIs(body="Easy Reply"),
        predicates=predicates.Equal({"method": "POST", "body": "hmm"})))

with servers.WindowsServer("C:\\temp\\mountebank-v1.13.0-win-x64"):
    with clients.Http("http://localhost", impostor) as client:
        result_1 = client.post_to_impostor(impostor, data="hmm")
        print result_1.text
```
