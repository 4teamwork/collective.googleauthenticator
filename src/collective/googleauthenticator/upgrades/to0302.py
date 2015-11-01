
def upgrade(setup_context):
    setup_context.runImportStepFromProfile(
        'profile-collective.googleauthenticator.upgrades:0302',
        'actions',
        run_dependencies=False,
        purge_old=False)
