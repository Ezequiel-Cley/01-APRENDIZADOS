# Instalando Configurado o PySpark

## 01. Instalações Padrões:

01.1. Python Instalador:

&nbsp; 1.1.1. Link em acesso 2025-11-16: https://www.python.org/downloads

01.2. Java (JDK versão 17) Instalador:

&nbsp; 1.2.1. Link em acesso 2025-11-16: https://www.oracle.com/java/technologies/javase/jdk17-0-13-later-archive-downloads.html

01.3. Apache Spark 4:

&nbsp; 1.3.1. Link em acesso 2025-11-16: https://spark.apache.org/downloads.html

01.4. Hadoop 3:

&nbsp; 1.4.1. Link em acesso 2025-11-16: https://github.com/cdarlint/winutils/tree/master/hadoop-3.3.6/bin

## 02. Criações de pastas:

02.1. Dentro do Disco local criar uma pasta  chamada "spark": C:\\spark

02.2. Dentro do Disco Local cria uma pasta chamada "hadoop" e dentro dessa pasta criar uma pasta chamada "bin" e incluir as informações baixadas nessa pasta: C:\\hadoop\\bin
	

## 03. Definições de Variaveis de Ambientes

03.1. HADOOP\_HOME = C:\\hadoop\\bin

03.2. SPARK\_HOME = C:\\spark

03.3. JAVA\_HOME = C:\\Program Files\\Java\\jdk-17

## 04. Incluir Path de sistemas na variaveis de ambientes com as variaveis criadas acima, apotando a pasta "bin"

&nbsp;	03.1. %HADOOP\_HOME%\\bin

&nbsp;	03.2. %SPARK\_HOME%\\bin

 	03.3. %JAVA\_HOME%\\bin



## 05. Abrir o CMD e escrever Pyspark e ser feliz...

