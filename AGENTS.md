<!-- local-deploy-policy-2026-10-12 -->
## Política de deploy local e GitHub Actions (12/10/2026)

- Não usar GitHub Actions neste repositório para CI, deploy, agendamentos ou qualquer outra automação. Não criar, habilitar ou executar workflows em `.github/workflows`.
- Fazer deploy diretamente de um computador local autorizado para AWS, Cloudflare ou outro provedor do projeto, usando os scripts e as credenciais locais aprovadas.
- Antes de publicar, confirmar a conta, o ambiente e o destino, executar as validações locais adequadas e identificar a versão a implantar. Depois, verificar o resultado no provedor.
- Se faltar um procedimento local de deploy, implementá-lo e documentá-lo antes da próxima publicação. Não reativar GitHub Actions para contornar essa falta.
- Referências antigas a GitHub Actions em outros arquivos são legado e não anulam esta política.
<!-- /local-deploy-policy-2026-10-12 -->

