# RPG_MINSAIT
Elaboração de script em Python - RPG

##### INÍCIO LOAD DO PROGRAMA ##### para utilizar no arquivo prompt.ipynb

from RPG_index import SerVivo
from RPG_index import Personagem
from RPG_index import Monstro
from RPG_index import Goblin
from RPG_index import Lobo

##### FIM DO LOAD DO PROGRAMA #####


LISTA DE MÉTODOS


1 - SERES VIVOS 
1.1 MOSTRAR SERES VIVOS
Malvo.mostrar_seres_vivos()   
-->   # Exibe todos os seres vivos, independente da classe, presentes no jogo.
# Qualquer ser vivo pode chamar esse método.

1.1 MOSTRAR SERES VIVOS
Ninim.mostrar_seres_vivos()   
-->   # Exibe todos os seres vivos, independente da classe, presentes no jogo.
-->   # Qualquer ser vivo pode chamar esse método.

1.2 MOSTAR ATRIBUTOS
Victor.mostrar_atributos()    
-->   # Exibe os pontos de vida e os pontos de ataque atuais do ser vivo que chamou o método.
-->   # Qualquer ser vivo pode chamar esse método.
      

2 - PERSONAGENS 
2.1 ADICIONAR PERSONAGEM
Victor = Personagem(name="Víctor", health_points=40, attack_points=20) 
-->   # Adiciona um ser vivo à classe "PERSONAGEM" 

Malvo = Personagem(name="Malvo", health_points=20, attack_points=10)  
-->   # Adiciona um ser vivo à classe "PERSONAGEM"

2.2 MOSTRAR PERSONAGENS
Victor.mostrar_personagens()  
-->   # Exibe todos os seres vivos da classe "PERSONAGEM" presentes no jogo.
-->   # Somente seres vivos da classe "PERSONAGEM" podem chamar esse método.

2.3 EXCLUIR PERSONAGENS
Victor.excluir_personagem(deleted="Malvo")  
-->   # Elimina o "PERSONAGEM" indicado no atributo "deleted" do jogo.
-->   # Somente seres vivos da classe "PERSONAGEM" podem chamar esse método.


3 - MONSTROS
3.1 ADICIONAR MONSTRO
Garu = Lobo(name="Garu", health_points=20, attack_points=15, power_points=7) 
-->   # Adiciona um ser vivo à classe "MONSTRO", com a espécie "LOBO".

Ninim = Goblin(name="Ninim", health_points=20, attack_points=5, intelligence_points=7) 
-->   # Adiciona um ser vivo à classe "MONSTRO", com a espécie "GOBLIN".

3.2 MOSTRAR MONSTROS
Garu.mostrar_monstros()       
-->   # Exibe todos os seres vivos da classe "MONSTRO" presentes no jogo.
-->   # Somente seres vivos da classe "MONSTRO" podem chamar esse método.

3.3 EXCLUIR MONSTRO
Garu.excluir_monstro(deleted="Ninim")  
-->   # Elimina o "MONSTRO" indicado no atributo "deleted" do jogo.
-->   # Somente seres vivos da classe "MONSTRO" podem chamar esse método.

3.4 ATACAR
Garu.atacar(target="Víctor")  
-->   # Com esse método, o "MONSTRO" que chamou o método realiza um ataque no "PERSONAGEM" indicado no atributo "target", causando perda de health_points em "target", de acordo com os "attack_points" do "MONSTRO".
-->   # Somente MONSTROS podem atacar, e somente PERSONAGENS podem sofrer o ataque.
-->   # Agora, "Víctor" tem 5 health_points.
