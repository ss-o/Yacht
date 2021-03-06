from fastapi import APIRouter, Depends, HTTPException, Form
from typing import List
from ..actions.compose import (
    get_compose_projects,
    compose_action,
    compose_app_action,
    get_compose,
    write_compose,
    delete_compose,
)
from fastapi_jwt_auth import AuthJWT
from ..auth import auth_check
from ..db.schemas.compose import *

router = APIRouter()


@router.get("/")
def get_projects(Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return get_compose_projects()


@router.get("/{project_name}")
def get_project(project_name, Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return get_compose(project_name)


@router.get("/{project_name}/actions/{action}")
def get_compose_action(project_name, action, Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    if action == "delete":
        return delete_compose(project_name)
    else:
        return compose_action(project_name, action)


@router.post("/{project_name}/edit", response_model=ComposeRead)
def write_compose_project(
    project_name, compose: ComposeWrite, Authorize: AuthJWT = Depends()
):
    auth_check(Authorize)
    return write_compose(compose=compose)


@router.get("/{project_name}/actions/{action}/{app}")
def get_compose_app_action(project_name, action, app, Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return compose_app_action(project_name, action, app)
