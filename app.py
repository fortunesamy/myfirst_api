from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from marshmallow import Schema, fields, ValidationError
from flask_sqlalchemy import SQLAlchemy