**Sistema de Mensagens Distribuídas com Exclusão Mútua**
Este projeto implementa um sistema de mensagens distribuídas com suporte a comunicação unicast, multicast e broadcast, além de um mecanismo de exclusão mútua distribuída utilizando relógios lógicos de Lamport.

**Visão Geral**
O sistema é composto por múltiplos clientes que se comunicam por meio de canais e acessam recursos compartilhados de forma coordenada. Utiliza conceitos fundamentais de sistemas distribuídos, como sincronização de eventos, ordenação lógica e controle de concorrência.

**Componentes Principais**
DistributedMessagingSystem: Núcleo do sistema, gerencia clientes, canais, recursos e relógio lógico global.
Client: Representa um nó distribuído que envia e recebe mensagens.
Message: Contém dados, remetente, timestamp e tipo da mensagem.
Channel: Suporta comunicação multicast.
ResourceManager: Controla acesso exclusivo a recursos compartilhados.
LogicalClock: Implementa relógios lógicos de Lamport.
MessageBuffer: Armazena e ordena mensagens por timestamp.

**Funcionalidades**
Registro de clientes
Envio de mensagens:
Unicast
Multicast (por canal)
Broadcast
Gerenciamento de recursos: Requisição e liberação com exclusão mútua
Ordenação de eventos com relógios lógicos

**Requisitos Funcionais**
Envio e recebimento de mensagens
Gerenciamento de canais e assinaturas
Exclusão mútua para acesso a recursos
Sincronização com relógios lógicos

**Requisitos Não Funcionais**
Confiabilidade e entrega garantida
Escalabilidade e desempenho
Consistência e observabilidade
