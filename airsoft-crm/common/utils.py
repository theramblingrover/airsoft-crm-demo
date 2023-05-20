

def get_player_id(player):
    return f'AK-{str(1+player.pk*111).rjust(7, "0")}'


def get_player_hash(player):
    from hashlib import sha256
    from base64 import b32encode
    return (
        b32encode(sha256(
            'Club'.encode('utf-8')
        ).digest()).decode().strip('=') + '-' +
        b32encode(sha256(
            (player.email+player.nick+player.telegram).lower(
            ).encode('utf-8')
        ).digest()).decode().strip('=')
    )
