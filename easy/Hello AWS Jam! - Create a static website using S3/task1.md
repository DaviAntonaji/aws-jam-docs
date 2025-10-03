Overview
Your company has recently patented Jam Fuel! This is a means to use bananas to fuel automobiles but you have no web presence. You need to stand up a static website as a landing area ASAP until the full-blown web content is developed. HURRY!


Background
Your product is taking off and you need to set up a static website ASAP.

Services You Should Use
S3

Your Tasks
Here are your steps to say Hello to the World using AWS:

1) Create a bucket (only create one). Your bucket name must start with "aws-jam-" (e.g., aws-jam-mywebsite-123)

2) Enable static website hosting on your bucket

3) Enable public access to your bucket by editing the "Block Public Access" settings

4) Add a bucket policy that makes your bucket content publicly available. Here is the policy to use:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [ "s3:GetObject" ],
"Resource": [ "arn:aws:s3:::Bucket-Name/*" ]
        }
    ]
}

5) Create an index.html file and upload it to your bucket.
Here is an HTML example to use:



   


   
Hello AWS Jam!

   
Now hosted on Amazon S3!



6) Create an upload an error file using the same file name when you configured static hosting on your bucket.
Here is an HTML example to use:



   


   
You have an Error :(

   
UGH!



7) Test your Jam's endpoint and save that endpoint for Jam Submission in the next step.
At the bottom of the Properties tab of your bucket, you can find your Bucket's website endpoint.

Task Validation
In the "task section" on the challenge builder menu, you can paste the URL of your S3 bucket into the text box and an automated script will check to see if the challenge is complete.

resolucao:


Pelo Console da AWS (mais rápido)

Crie o bucket

S3 → Create bucket

Bucket name: algo como aws-jam-meusite-123 (tem que começar com aws-jam-)

Region: escolha a sua

Deixe o resto padrão e crie.

Habilite static website hosting

Abra o bucket → aba Properties

Role até Static website hosting → Edit → marque Enable

Hosting type: Host a static website

Index document: index.html

Error document: error.html

Save changes

Permitir acesso público (desligar bloqueio)

Aba Permissions → Block public access (bucket settings) → Edit

Desmarque as 4 opções, confirme digitando confirm, Save.

Política pública do bucket

Ainda em Permissions → Bucket policy → Edit

Cole a política abaixo trocando Bucket-Name pelo NOME do seu bucket:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::Bucket-Name/*"]
    }
  ]
}


Save changes.

Crie e suba o index.html
Crie um arquivo index.html com este conteúdo:

<!doctype html>
<html>
  <head><meta charset="utf-8"><title>Hello</title></head>
  <body>
    <h1>Hello AWS Jam!</h1>
    <p>Now hosted on Amazon S3!</p>
  </body>
</html>


Aba Objects → Upload → selecione index.html → Upload.

Crie e suba o error.html
Crie error.html com:

<!doctype html>
<html>
  <head><meta charset="utf-8"><title>Error</title></head>
  <body>
    <h1>You have an Error :(</h1>
    <p>UGH!</p>
  </body>
</html>


Upload do error.html no bucket.

Teste e guarde o endpoint

Aba Properties → seção Static website hosting

Copie o Bucket website endpoint (parece com http://aws-jam-meusite-123.s3-website-<região>.amazonaws.com)

Abra no navegador e use essa URL para a validação do Jam.