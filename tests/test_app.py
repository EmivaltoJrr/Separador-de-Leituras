import sys
import unittest
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from docx import Document  # noqa: E402

import processamento  # noqa: E402
from main import app  # noqa: E402


class TestProcessamento(unittest.TestCase):
    def test_jo_e_joao_e_jo_acentuado_e_jo(self):
        self.assertEqual(processamento.identificar_leitura("Jo 3,16")[:2], ("Evangelho", "João 3,16"))
        self.assertEqual(processamento.identificar_leitura("Jó 19,25")[:2], ("Profetas", "Jó 19,25"))
        self.assertEqual(processamento.identificar_leitura("Job 1,1")[0], "Profetas")
        self.assertEqual(processamento.identificar_leitura("1Jo 4,8")[0], "Cartas")

    def test_categorias_batem_com_colunas_do_word(self):
        leituras, erros = processamento.classificar_texto("GN 11, 30\nIS 44, 6\nHB 11, 32\nMT 1, 14")
        self.assertEqual(erros, [])
        org = processamento.organizar(leituras, processamento.FORMATO_ABREVIADO)
        self.assertEqual(org, {"Históricos": ["GN 11, 30"], "Profetas": ["IS 44, 6"],
                               "Cartas": ["HB 11, 32"], "Evangelho": ["MT 1, 14"]})

    def test_erros_informam_numero_da_linha(self):
        _, erros = processamento.classificar_texto("Gn 1,1\n\n1S, 5, 2S")
        self.assertEqual(erros, [{"linha": 3, "texto": "1S, 5, 2S"}])


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_gerar_com_sigla_desconhecida_retorna_422(self):
        r = self.client.post("/api/gerar", json={"texto": "Gn 1,1\nXx 2,2"})
        self.assertEqual(r.status_code, 422)
        self.assertEqual(r.get_json()["erros"][0]["linha"], 2)

    def test_gerar_ignorando_desconhecidas(self):
        r = self.client.post("/api/gerar", json={"texto": "Gn 1,1\nXx 2,2", "ignorar_desconhecidas": True})
        self.assertEqual(r.status_code, 200)

    def test_gerar_docx_em_memoria(self):
        texto = Path(__file__).resolve().parent.parent.joinpath("LEITURAS.txt").read_text(encoding="utf-8")
        texto = texto.replace("1S, 5, 2S", "1SM 5, 2S")
        r = self.client.post("/api/gerar", json={"texto": texto, "formato": "completo"})
        self.assertEqual(r.status_code, 200)
        self.assertIn("attachment", r.headers["Content-Disposition"])
        doc = Document(BytesIO(r.data))
        conteudo = "\n".join(c.text for row in doc.tables[0].rows for c in row.cells)
        self.assertIn("Josué 13, 2+", conteudo)
        self.assertIn("Isaías 44, 6", conteudo)
        self.assertIn("Apocalipse 19, 12", conteudo)


if __name__ == "__main__":
    unittest.main()
