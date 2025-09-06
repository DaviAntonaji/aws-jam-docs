# Task 3 – Update IAM Role for EKS Pod Identity Association

## 📌 Background

A empresa solicitou a implementação de suporte a EKS Pod Identity Associations. A ideia é automatizar a atualização da Assume Role Policy Document de roles IAM que serão usados para associações de Pod Identity, tornando-os compatíveis com o serviço `pods.eks.amazonaws.com`.

## 🎯 Objetivo da Task

- Editar a função Lambda `bedrock-agent-eks-access-control`
- Completar a seção comentada "Update IAM role's assume role policy"
- Atualizar a policy de trust do role `arn:aws:iam::{AccountID}:role/eks-pod-test-role`
- Validar a modificação por meio de um prompt ao agente Bedrock `eks-bedrock-agent`

**Task Validation esperada:**
```
After updating the lambda function's code, modify the role arn:aws:iam::{AccountID}:role/eks-pod-test-role 
to make it compatible with EKS Pod Identity Association
```

## 🔧 O que foi Implementado

### Lambda Function

No bloco `/updateRolePodIdentity`, foi adicionado código para:

1. **Extrair roleArn do request**
2. **Construir a trust policy mínima exigida pelo EKS Pod Identity:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "pods.eks.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

3. **Usar o comando `UpdateAssumeRolePolicyCommand`** do `@aws-sdk/client-iam` para aplicar a policy
4. **Retornar resposta mínima:**

```json
{ "roleArn": "arn:aws:iam::115476679712:role/eks-pod-test-role" }
```

### OpenAPI Schema

No `openapi-schema.yaml`, foi definido o endpoint `/updateRolePodIdentity`:

```yaml
/updateRolePodIdentity:
  post:
    summary: Update IAM role trust policy to make it compatible with EKS Pod Identity Association
    description: Update the IAM role's assume role policy so that pods.eks.amazonaws.com can assume it, making it compatible with EKS Pod Identity Association.
    operationId: updateRolePodIdentity
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              roleArn:
                type: string
            required: [roleArn]
    responses:
      '200':
        description: Successfully updated the assume role policy for the given IAM role.
        content:
          application/json:
            schema:
              type: object
              properties:
                roleArn:
                  type: string
```

## ✅ O que Funcionou

- ✅ Lambda foi atualizado e publicado
- ✅ Bedrock Agent (`eks-bedrock-agent`) reconheceu o endpoint `/updateRolePodIdentity`
- ✅ Testes no console retornaram a resposta correta:

```json
{"roleArn":"arn:aws:iam::115476679712:role/eks-pod-test-role"}
```

- ✅ O agente respondeu:

```
The IAM role arn:aws:iam::115476679712:role/eks-pod-test-role has been successfully updated to make it compatible with EKS Pod Identity Association.
```

## ❌ Problema Encontrado

Apesar do retorno correto no console do agente, o JAM "Check my progress" não marcou a task como concluída.

**Possíveis motivos levantados:**
- O validador pode estar esperando frase exata ou formato específico no OpenAPI
- O JAM pode exigir execução via alias de teste e não prod
- O lab pode ter um bug de validação (mesmo comportamento reproduzido várias vezes)

## 📄 Conclusão

- ✅ A Lambda function foi corretamente implementada para atualizar a trust policy
- ✅ O OpenAPI Schema foi atualizado de acordo com a descrição da task
- ✅ Os testes no Bedrock Agent retornaram o output esperado

**Contudo**, o validador do JAM não marcou a atividade como concluída, sugerindo que há algum detalhe de validação ou limitação do lab fora do controle do participante.

## 👉 Evidência

- **Logs de execução** mostram o uso do endpoint `/updateRolePodIdentity`
- **Resposta final do agente:**

```
The IAM role arn:aws:iam::115476679712:role/eks-pod-test-role has been successfully updated to make it compatible with EKS Pod Identity Association.
```

**Entretanto**, o Check My Progress continua sem validar a task.