import json
import os
import hashlib

ADMIN_PATH = os.path.join(os.path.dirname(__file__), '..', 'core', 'admin.json')


def _load_admin():
    if not os.path.exists(ADMIN_PATH):
        return {"password_hash": ""}
    with open(ADMIN_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def _save_admin(admin_data):
    with open(ADMIN_PATH, 'w', encoding='utf-8') as f:
        json.dump(admin_data, f, ensure_ascii=False, indent=2)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_password_set():
    admin = _load_admin()
    return admin.get("password_hash")


def set_password(password):
    admin = _load_admin()
    admin["password_hash"] = hash_password(password)
    _save_admin(admin)


def validate_password(password):
    admin = _load_admin()
    return admin.get("password_hash") == hash_password(password)


def change_password(old_password, new_password):
    if not validate_password(old_password):
        return False
    set_password(new_password)
    return True
