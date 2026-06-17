from fastapi import HTTPException

from app.services.empresa_service import (
    create_empresa_service,
    create_empresa_completo_service,
    get_empresas_service,
    get_empresa_by_id_service,
    update_empresa_service,
    delete_empresa_service
)


def create_empresa_controller(data):
    try:
        empresa = create_empresa_service(data)

        return {
            "message": "Empresa criada com sucesso",
            "empresa": empresa
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def create_empresa_completo_controller(data):
    try:
        empresa = create_empresa_completo_service(data)

        return {
            "message": "Usuário e Empresa criados com sucesso",
            "empresa": empresa
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_empresas_controller():
    try:
        empresas = get_empresas_service()

        return {
            "message": "Empresas listadas com sucesso",
            "empresas": empresas
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_empresa_by_id_controller(id_empresa):
    try:
        empresa = get_empresa_by_id_service(id_empresa)

        return {
            "message": "Empresa encontrada com sucesso",
            "empresa": empresa
        }

    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_empresa_controller(id_empresa, data):
    try:
        return update_empresa_service(id_empresa, data)

    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def delete_empresa_controller(id_empresa):
    try:
        return delete_empresa_service(id_empresa)

    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
