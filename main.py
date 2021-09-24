import asyncio
from asyncua import Server, ua
from random import randint

async def main():
    serveur = Server()
    await serveur.init()
    serveur.set_server_name('Alexandre Serv')

    url='opc.tcp://10.4.1.152:4840'
    serveur.set_endpoint((url))
    serveur.set_security_policy([ua.SecurityPolicyType.NoSecurity,
                                ua.SecurityPolicyType.Basic256Sha256_Sign,
                                ua.SecurityPolicyType.Basic256_SignAndEncrypt])

    nom_espace_adresse = 'Alexandre Serv'
    espace_adresse = await serveur.register_namespace(nom_espace_adresse)
    moteur1 = await serveur.nodes.objects.add_object(espace_adresse, 'Moter1')
    noeud_variabl_temperature = await moteur1.add_variable(espace_adresse, 'Temperature', 0)
    noeud_variable_est_en_marche = await moteur1.add_variable(espace_adresse, 'enMarche', False)
    async def active_moteur(parent):
        print('moteur maintenent en marche')
        await noeud_variable_est_en_marche.set_value(True)

    noeud_fonction_active_moteur = await moteur1.add_methode(espace_adresse, 'mettre en marche', active_moteur, [],[ua.VariantType.boolean])

    async with serveur:
        while True:
            temparature = randint(-30, 45)
            await noeud_variable_temperature.set_value(temperature)
            await asyncio.sleep(5)
        print('ehllo')


if __name__ == '__main__'
    try:
        asyncio.run(main())
        except key

