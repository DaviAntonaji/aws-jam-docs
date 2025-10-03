Task 2: Resolve the overly permissive access
Possible Points
56
Clue Penalty
0
Points Available
56
Check my progress

Task and Clues
Background
Now that you have found overly permissive access that could potentially allow unauthorized access to the Jam challenge bucket, you need to resolve this overly permissive access policies that may be leaving the bucket open to unauthorized access.

Your Task
Your task is to make sure that there are no active findings in IAM Access Analyzer which lists JAM challenge S3 buckets as the resource.

Getting Started
Visit the Jam challenge bucket in the S3 console and try to resolve the overly permissive access as mentioned in IAM Access Analyzer findings.

Inventory
AWS IAM Access Analyzer has been already created for you. You can find the Jam challenge S3 bucket in the Output Properties section.

Services you should use
AWS IAM, IAM Access Analyzer, Amazon S3

Task Validation
In order to confirm a change you made to resolve the finding, you may have to rescan the resource reported in the finding by using the Rescan link in the Findings details page of IAM Access Analyzer.

The task will auto complete once you fix the overly permissive access in the Challenge bucket and the Rescan shows a success status. You can also validate your progress by selecting the Check my progress button.

🔧 Como corrigir

Você precisa editar a Bucket Policy e remover esse statement que dá acesso para a outra conta.

Opção 1: Via Console

Vá em S3 → seu bucket → Permissions → Bucket Policy.

Clique em Edit.

Apague todo o bloco Statement que contém:

{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::173358130759:root"
    },
    "Action": "s3:ListBucket",
    "Resource": "arn:aws:s3:::challenge1bucket-82e757a0-a0a6-11f0-b67e-0272e0e36f87"
}


Salve a policy (pode até deixar vazia { "Version": "2012-10-17", "Statement": [] }).

Opção 2: Via CLI
aws s3api delete-bucket-policy \
  --bucket challenge1bucket-82e757a0-a0a6-11f0-b67e-0272e0e36f87

✅ Depois

Volte no IAM → Access Analyzer.

Selecione o finding do bucket.

Clique em Rescan.

O finding deve desaparecer e o Task 2 será concluído automaticamente.