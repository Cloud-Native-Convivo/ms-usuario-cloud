# Política de Seguridad

## Reporte de Vulnerabilidades

La seguridad de este microservicio es prioritaria. Si descubres una vulnerabilidad de seguridad, por favor repórtala de forma responsable.

### Cómo Reportar

**No abras un issue público para reportar vulnerabilidades de seguridad.**

Utiliza el mecanismo oficial de reporte privado:

1. **Private Vulnerability Reporting (Recomendado)**
   - Dirígete a la pestaña [Security Advisories](../../security/advisories) del repositorio.
   - Haz clic en **"Report a vulnerability"**.
   - Proporciona la descripción detallada, pasos de reproducción, impacto potencial y propuesta de mitigación si dispones de ella.

### Plazos de Respuesta

- **Acuse de recibo inicial**: dentro de las primeras 48 horas hábiles.
- **Evaluación y triaje**: dentro de 7 días hábiles.
- **Parche y divulgación coordinada**: una vez probado y desplegado el fix en `develop` y `main`.

## Versiones Soportadas

| Versión | Soportada |
| ------- | --------- |
| Rama `develop` / Último tag `main` | Sí |
| Versiones anteriores sin soporte | No |

## Características de Seguridad Habilitadas

Este repositorio cuenta con las directrices de [GitHub Security Lab](https://securitylab.github.com/):

- **Branch Protection**: protección estricta en ramas `main` y `develop` (requiere Pull Request, revisión aprobada, prohíbe force-push y eliminaciones).
- **Private Vulnerability Reporting**: canal privado y cifrado para reporte y gestión de Security Advisories.
- **Secret Scanning con Push Protection**: escaneo activo y bloqueo inmediato en push para más de 300 tipos de tokens y credenciales.
- **Dependabot**: alertas automatizadas y security updates periódicos ante CVEs conocidos.
- **Code Scanning (CodeQL)**: análisis estático automatizado de vulnerabilidades y seguridad en flujos de GitHub Actions.

## Buenas Prácticas para Contribuidores

- Nunca commitear credenciales, variables `.env` ni tokens de acceso al repositorio.
- Seguir las políticas operativas y normativas descritas en [AGENTS.md](AGENTS.md).
- Mantener las dependencias de `requirements.txt` actualizadas y libres de CVEs críticos/altos.
- Validar siempre los cambios con la suite de pruebas (`pytest`) y linter (`ruff check .`) antes de abrir un PR.
