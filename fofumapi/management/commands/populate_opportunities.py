from django.core.management.base import BaseCommand
import requests
from fofumapi.models.blockchain import Blockchain
from fofumapi.models.protocol import Protocol
from fofumapi.models.opportunity import Opportunity

class Command(BaseCommand):
    help = 'Populates the database with blockchain, protocol, and opportunity data.'

    DEFI_LLAMA_URL = "https://api.llama.fi/protocols"

    def fetch_defi_data(self):
        response = requests.get(self.DEFI_LLAMA_URL)
        if response.status_code == 200:
            return response.json()
        else:
            self.stderr.write(f"Failed to fetch data: {response.status_code}")
            return []

    def populate_blockchains(self, data):
        blockchains = {}
        for protocol in data:
            blockchain_name = protocol.get('chain', 'Unknown')
            if blockchain_name not in blockchains:
                blockchain, created = Blockchain.objects.get_or_create(
                    name=blockchain_name,
                    defaults={"symbol": blockchain_name[:3].upper()}  # Example symbol
                )
                blockchains[blockchain_name] = blockchain
        return blockchains

    def populate_protocols_and_opportunities(self, data, blockchains):
        for protocol in data:
            protocol_name = protocol['name']
            description = protocol.get('description', '')
            website = protocol.get('url', '')
            blockchain_name = protocol.get('chain', 'Unknown')

            blockchain = blockchains.get(blockchain_name)
            if not blockchain:
                self.stderr.write(f"Blockchain {blockchain_name} not found, skipping protocol {protocol_name}.")
                continue

            protocol_obj, created = Protocol.objects.get_or_create(
                name=protocol_name,
                blockchain=blockchain,
                defaults={"description": description, "website": website}
            )

            tvl = protocol.get('tvl', 0)
            apy = protocol.get('apy', 0)
            token = protocol.get('symbol', 'N/A')

            Opportunity.objects.create(
                protocol=protocol_obj,
                name=f"{protocol_name} Opportunity",
                opportunity_type="farming",
                apy=apy,
                risk_score=80,
                liquidity=tvl,
                token=token
            )

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching data from DefiLlama...")
        defi_data = self.fetch_defi_data()

        self.stdout.write("Populating blockchains...")
        blockchains = self.populate_blockchains(defi_data)

        self.stdout.write("Populating protocols and opportunities...")
        self.populate_protocols_and_opportunities(defi_data, blockchains)

        self.stdout.write("Data population complete.")
