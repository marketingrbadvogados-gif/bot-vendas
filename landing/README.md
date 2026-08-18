# Página de vendas — O Guia do Dinheiro que o Aposentado Pode Estar Deixando Para Trás

Página estática, um arquivo só (`index.html`), sem dependências além do Google Fonts.
Pode ser publicada em qualquer lugar: Netlify, Vercel, GitHub Pages, Hostinger,
ou servida pelo próprio servidor que já roda o `main.py`.

## Antes de publicar, mude 3 coisas

1. **Link do checkout** — no fim do `index.html`, na linha:

   ```js
   var CHECKOUT = "";
   ```

   Cole o link do seu checkout (Kiwify, Hotmart, Asaas, Cartpanda...). Enquanto
   ficar vazio, todos os botões apenas rolam a página até a oferta.

2. **Preço** — hoje está `R$ 47` (ancorado em `R$ 211`). Aparece em 5 lugares:
   os quatro botões, a barra fixa do rodapé e o bloco da oferta. Busque por
   `47` no arquivo.

3. **Prova social** — a página não traz depoimento nenhum, de propósito:
   inventar depoimento é ilegal e destrói confiança. Assim que tiver prints reais
   de compradores, o melhor lugar para eles é logo depois da seção
   "De onde vem a informação", antes da oferta.

## O que a página faz

- Mobile-first, corpo em 19px e alvos de toque grandes — o público é 60+.
- Tema claro e escuro, seguindo a preferência do aparelho.
- Diagnóstico interativo de 12 itens (o mesmo que abre o eBook): conta o que a
  pessoa marcou e devolve um veredito. É o momento de maior engajamento da
  página e qualifica o comprador antes do preço.
- Barra fixa com preço e botão, que aparece depois da primeira rolagem e some
  quando o bloco da oferta está na tela.
- Nenhum dado sai do aparelho do visitante.

## Cuidado com a copy

O eBook é material informativo e diz, na primeira página, que não promete
recebimento. A página de vendas segue a mesma régua: fala em **conferir**,
nunca em **garantir dinheiro**. Se for adaptar o texto, mantenha isso — promessa
de resultado em material ligado a escritório de advocacia é problema de ética
profissional, além de gerar reembolso e reclamação.
