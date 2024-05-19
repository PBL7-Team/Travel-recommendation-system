from api_oauth2.scopes import (
    scopes as oauth_scopes,
    system_scopes as oauth_system_scopes,
    default_scopes as oauth_default_scopes,
)

# from businesses.scopes import (
#     scopes as businesses_scopes,
#     system_scopes as businesses_system_scopes,
#     default_scopes as businesses_default_scopes,
# )


scopes = {
    **oauth_scopes,

}

default_scopes = {
    **oauth_default_scopes,

}

# These scope only available for system apps
system_scopes = {
    **oauth_system_scopes,
}
