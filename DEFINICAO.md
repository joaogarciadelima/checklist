# Definição completa do projeto

- Objetivo

  - Transformação digital no processo de recepção de veículos na oficina

- Funcionalidades:
 
  - Recepção do cliente (primeira funcionalidade a liberar)
    - Identificação do cliente previamente cadastrado
    - Cadastro de cliente novo
    - Identificação do veículo pela placa previamente cadastrada(a placa do veículo será uma chave única)
    se já estiver cadastrada para outro cliente deve haver a possibilidade de transferência de titularidade.
    - Cadastro de novo veículo.

  - dados da ordem de serviço(implementação a analisar viabilidade)
    - Fotos do veículo(fotos do painel para confirmar km etc)
    - Gravação de voz do relato do cliente
  
## Detalhes técnicos:
  - Interface HTTP
  - online no banco de dados
  - servidor próprio em cada instalação do ERP
  - **Banco do ERP SQL SERVER**
  - Definido tamanho do tablet de 10’’ para parâmetro mobile

## Desafios

- Algumas implementações na fase inicial e outras a serem pensadas

  - Fase inicial:
    - Autenticação dos usuários do sistema web e do ERP
    - Cadastrar um novo cliente, pois os dados na abertura da OS são mínimos, normalmente os clientes não querem e não
    tem tempo para detalhar os dados ao entregar os veículos.
    - Cadastrar um novo cliente se o cadastro da OS já começou.
    - Cadastrar um novo veículo em os já iniciada.
    - Gravar a voz do cliente com o problema do carro se houver(implementação futura)
    - Usabilidade (talvez botões grandes de dashboard )
    - Navegar entre formulários, provavelmente será usado um tablet para a recepção e primeiro cadastro das informações da ordem de serviço
    - Localização de clientes
    - Localização de OS
    - Localização de veículos

# Futuro

- Itens a avaliar para implementação futura

  - 2ª fase:
    - Precisa aprovar orçamento
    - Prazo para entrega do veículo
    - Histórico do cliente
    - Exibição do histórico do veículo na interface web(histórico já existe no ERP)
    - Identificação da OS por cliente ou veículo
    - Checagem de entrega, para qualificar e garantir o processo
    - Assinatura do cliente na entrega do veículo
    - Registro de horas dos mecânicos
    - Solicitação e registro de peças para a OS
    - Autorizações de orçamento pela web
    - Painel de acompanhamento
    - Agenda de trabalhos
    - Agenda de entregas do dia para o atendente e fone do cliente
    - Integração com sistema de aviso de veículo liberado ou pronto