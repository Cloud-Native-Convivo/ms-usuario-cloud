def test_app_arranca_con_middlewares_de_seguridad(client):
    response = client.get("/docs")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
