from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app import main


@pytest.mark.asyncio
@pytest.mark.parametrize("eureka_falla", [False, True])
async def test_lifespan_con_eureka(eureka_falla):
    eureka = MagicMock()
    eureka.init_async = AsyncMock(side_effect=RuntimeError("sin eureka") if eureka_falla else None)
    eureka.stop_async = AsyncMock(side_effect=RuntimeError("ya detenido") if eureka_falla else None)
    with (
        patch.object(main.settings, "eureka_url", "http://eureka"),
        patch.object(main, "eureka_client", eureka),
    ):
        async with main.lifespan(main.app):
            pass  # una falla de Eureka no debe impedir el arranque

    eureka.init_async.assert_awaited_once()
    eureka.stop_async.assert_awaited_once()


@pytest.mark.asyncio
async def test_lifespan_sin_eureka_no_registra():
    eureka = MagicMock()
    eureka.init_async = AsyncMock()
    eureka.stop_async = AsyncMock()
    with (
        patch.object(main.settings, "eureka_url", ""),
        patch.object(main, "eureka_client", eureka),
    ):
        async with main.lifespan(main.app):
            pass

    eureka.init_async.assert_not_awaited()
    eureka.stop_async.assert_not_awaited()
