"""Example of usage of the Veolia API"""

import asyncio
import logging

from veolia_api.veolia_api import VeoliaAPI

logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    """Main function."""
    # Create an instance of the VeoliaAPI class
    api = VeoliaAPI("username", "password")

    try:
        # Fetch data for November 2024
        await api.fetch_all_data(2024, 11)

        # Display fetched data
        print(api.account_data.daily_consumption)
        print(api.account_data.monthly_consumption)
        print(api.account_data.alert_settings.daily_enabled)

    except Exception as e:
        logging.error("An error occurred: %s", e)
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
