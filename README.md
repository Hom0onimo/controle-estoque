CONTROLE DE ESTOQUE

Projeto que desenvolvi para o desafio tecnico da veloz.

A aplicação tem como objetivo calcular a quantidade de cada ingrediente que deve ser comprada para o próximo mês, levando em consideração o estoque atual, a meta definida e algumas situações específicas, como vencimento ou falta de estoque.

Funciona assim:

Para cada ingrediente são informados:

- Nome
- Unidade de medida
- Meta de estoque
- Estoque atual
- Consumo durante o mês
- Se o ingrediente venceu
- Se o ingrediente acabou antes do final do mês

A quantidade da compra é calculada de acordo com a situação:

Estoque normal:
é comprada apenas a diferença entre a meta e o estoque atual.

Ingrediente vencido:
o estoque restante é descartado e é necessário comprar novamente a quantidade definida como meta.

*Ingrediente que acabou antes do final do mês: 
é considerado o consumo do mês com um acréscimo de 20%, para evitar que o estoque fique abaixo do necessário no mês seguinte.

As unidades de medida são mantidas de acordo com cada ingrediente, podendo ser kg, litros, unidades ou outras.

 Tecnologias que utilizei: 

 Tudo descrito no desafio

- Python
- Django
- SQLite
- HTML
- CSS

O projeto não utiliza frameworks de frontend, mantendo a interface simples e focada na funcionalidade principal do desafio.

 Estrutura do projeto

A aplicação foi organizada separando a regra de negócio da parte responsável pela página.

A pasta `estoque` contém a aplicação principal do projeto. A lógica de cálculo das compras fica em `services.py`, enquanto `views.py` é responsável por buscar os ingredientes e enviar os resultados para a página.

Também foram adicionados testes automatizados para verificar os principais cenários do cálculo.

 Para executar:


git clone URL_DO_REPOSITORIO
cd controle-estoque
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

No fim:

acesse http://127.0.0.1:8000/