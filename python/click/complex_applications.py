import os
import click


class Repo(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or ".")
        self.debug = debug

    def __repr__(self):
        return f"Repo: {self.home}, debug: {self.debug}"

pass_repo = click.make_pass_decorator(Repo, ensure=True)


@click.group()
@click.option("--repo-home", envvar="REPO_HOME", default=".repo")
@click.option("--debug/--no-debug", default=False, envvar="REPO_DEBUG")
@click.pass_context
def cli(ctx, repo_home, debug):
    print(f"cli ctx: {ctx}")
    ctx.obj = Repo("test", debug)


@cli.command()
@click.argument("src")
@click.argument("dest", required=False)
@pass_repo
def clone(repo, src, dest):
    print(f"obj: {repo}")
    click.echo(isinstance(repo, Repo))
    print(f"src: {src}")
    print(f"dest: {dest}")


if __name__ == "__main__":
    cli()
