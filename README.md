
# Como usar o git

1. O primeiro passo a ser feito é baixar o git, isso pode ser feito 

no windows: através do link https://git-scm.com/download/win

no linux: ```sudo apt-install git ```

2. Após esse passo, você deve selecionar um diretorio de sua escolha, você pode fazer isso de 2 maneiras

<br>

no windows, utilize o comando "git bash here" é apenas precionar o botão direito do mouse

no linux/windows via prompt: ```cd diretorio/de/sua/escolha```

3. Agora inicialize um repositório local em sua maquina

```git init```

4. para começar a manipular os files do projeto, cloneo para seu computador
```git clone https://github.com/victorletichevsky/ProgMod2022.2.git```

5. Agora você já pode começar a fazer alterações no código, um comando muito util para o desenvolver do projeto será

```git status```

Obs: esse comando te permite ver quais arquivos foram alterados

6. você pode atualizat no github os arquivos que você alterou.

    + primeiro voce deve criar uma branch nova com o comando:
        + ```git checkout -b <nome da parte que esta sendo alterada>```
    + se o branch já estiver criado use:
        + ```git checkout <nome do branch>```
    + é ideal que você sempre intercale as operações com o git pull, para ter certeza que seu codigo esta sempre atualizado
        + ```git pull```
    + agora so falta o git push
        + ```git push```
        + talvez nessa hora apareça um erre e uma sugestão de comando, se esse for o caso é so exucutar essa sugestão