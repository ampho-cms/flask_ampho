"""Ampho Locale Bundle Commands
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import click
from typing import Tuple
from os import path
from ampho import Bundle, g, current_app
from babel.messages.frontend import CommandLineInterface as BabelCLI

_bundle = g.bundle  # type: Bundle


@_bundle.command('extract')
@click.argument('bundles', nargs=-1)
def extract_cmd(bundles: Tuple[str, ...]):
    """Extract messages to a POT file
    """
    for b_name in bundles or _bundle.app.bundles:
        b = current_app.get_bundle(b_name)
        if not b.locale_dir:
            continue

        out_f_path = path.join(b.locale_dir, f'{b_name}.pot')
        BabelCLI().run(['babel', 'extract', '--no-location', '--omit-header', '--sort-output',
                        '-F', _bundle.res_path('babel.ini'), '-o', out_f_path, b.root_dir])


@_bundle.command('init')
@click.argument('locale')
@click.argument('bundle')
def init_cmd(bundle: str, locale: str):
    """Init a new PO file
    """
    b = current_app.get_bundle(bundle)
    inp_f_path = path.join(b.locale_dir, f'{b.name}.pot')
    BabelCLI().run(['babel', 'init', '-D', bundle, '-l', locale, '-i', inp_f_path, '-d', b.locale_dir])


@_bundle.command('update')
@click.argument('locale')
@click.argument('bundles', nargs=-1)
def update_cmd(locale: str, bundles: Tuple[str, ...]):
    """Update an existing PO file
    """
    for b_name in bundles or _bundle.app.bundles:
        b = current_app.get_bundle(b_name)
        if not b.locale_dir:
            continue

        inp_f_path = path.join(b.locale_dir, f'{b.name}.pot')
        BabelCLI().run(['babel', 'update', '-D', b.name, '-l', locale, '-i', inp_f_path, '-d', b.locale_dir])


@_bundle.command('compile')
@click.argument('bundles', nargs=-1)
def compile_cmd(bundles):
    """Compile translations
    """
    for b_name in bundles or _bundle.app.bundles:
        b = current_app.get_bundle(b_name)
        if not b.locale_dir:
            continue

        BabelCLI().run(['babel', 'compile', '-D', b.name, '-d', b.locale_dir])
