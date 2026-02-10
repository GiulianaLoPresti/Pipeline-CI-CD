# Scriviamo una classe semplice che mi permetta di effettuare dei test con i CI/CD

class Testclass:
    def test_one(self):  # definisco un metodo (test esemplificativo)
        x="this"
        assert "h" in x

    def test_two(self):
        x="hello"
        assert x =="hello"

# Lo scopo è che questo test venga automatizzato si github, quindi committiamo
