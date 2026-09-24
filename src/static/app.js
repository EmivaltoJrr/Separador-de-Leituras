const $ = (id) => document.getElementById(id);

const texto = $("texto");
const btnGerar = $("btn-gerar");
const btnPrevia = $("btn-previa");

function payload() {
  return {
    texto: texto.value,
    formato: document.querySelector('input[name="formato"]:checked').value,
    ignorar_desconhecidas: $("ignorar").checked,
  };
}

function mostrarMensagem(msg, tipo) {
  const el = $("mensagem");
  el.textContent = msg;
  el.className = `mensagem ${tipo}`;
  el.hidden = !msg;
}

function limparFeedback() {
  mostrarMensagem("", "");
  $("erros").hidden = true;
}

// Seleciona a linha N (1-based) dentro do textarea para o usuário corrigir.
function irParaLinha(num) {
  const linhas = texto.value.split("\n");
  const inicio = linhas.slice(0, num - 1).reduce((acc, l) => acc + l.length + 1, 0);
  texto.focus();
  texto.setSelectionRange(inicio, inicio + linhas[num - 1].length);
  const alturaLinha = texto.scrollHeight / linhas.length;
  texto.scrollTop = Math.max(0, (num - 3) * alturaLinha);
}

function mostrarErros(erros) {
  const lista = $("lista-erros");
  lista.replaceChildren();
  for (const { linha, texto: t } of erros) {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.type = "button";
    const num = document.createElement("span");
    num.className = "num";
    num.textContent = `Linha ${linha}:`;
    btn.append(num, t);
    btn.addEventListener("click", () => irParaLinha(linha));
    li.append(btn);
    lista.append(li);
  }
  $("erros").hidden = erros.length === 0;
}

function mostrarPrevia(resumo, total) {
  const colunas = $("colunas");
  colunas.replaceChildren();
  for (const [categoria, itens] of Object.entries(resumo)) {
    const div = document.createElement("div");
    div.className = "coluna";
    const h3 = document.createElement("h3");
    h3.textContent = `${categoria} (${itens.length})`;
    const ul = document.createElement("ul");
    if (itens.length === 0) {
      const li = document.createElement("li");
      li.className = "vazio";
      li.textContent = "—";
      ul.append(li);
    }
    for (const item of itens) {
      const li = document.createElement("li");
      li.textContent = item;
      ul.append(li);
    }
    div.append(h3, ul);
    colunas.append(div);
  }
  $("total").textContent = `· ${total} leitura(s)`;
  $("previa").hidden = false;
}

async function enviar(url) {
  return fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload()),
  });
}

btnPrevia.addEventListener("click", async () => {
  limparFeedback();
  if (!texto.value.trim()) return mostrarMensagem("Cole ou carregue algumas leituras primeiro.", "erro");
  try {
    const resp = await enviar("/api/processar");
    const dados = await resp.json();
    mostrarPrevia(dados.resumo, dados.total);
    mostrarErros(dados.erros);
  } catch {
    mostrarMensagem("Não foi possível falar com o servidor.", "erro");
  }
});

btnGerar.addEventListener("click", async () => {
  limparFeedback();
  if (!texto.value.trim()) return mostrarMensagem("Cole ou carregue algumas leituras primeiro.", "erro");

  btnGerar.disabled = true;
  btnGerar.textContent = "Gerando…";
  try {
    const resp = await enviar("/api/gerar");
    if (!resp.ok) {
      const dados = await resp.json().catch(() => ({}));
      mostrarMensagem(dados.mensagem || "Erro ao gerar o documento.", "erro");
      mostrarErros(dados.erros || []);
      return;
    }
    const blob = await resp.blob();
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "leituras_preenchidas.docx";
    document.body.append(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(link.href);
    mostrarMensagem("Documento gerado! O download deve começar automaticamente.", "ok");
  } catch {
    mostrarMensagem("Não foi possível falar com o servidor.", "erro");
  } finally {
    btnGerar.disabled = false;
    btnGerar.textContent = "Gerar Documento Word";
  }
});

// O .txt é lido no navegador e jogado no textarea, assim o usuário pode corrigir antes de enviar.
$("arquivo").addEventListener("change", async (e) => {
  const arquivo = e.target.files[0];
  if (!arquivo) return;
  texto.value = await arquivo.text();
  e.target.value = "";
  limparFeedback();
});
