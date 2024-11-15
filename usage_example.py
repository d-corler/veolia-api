"""Example of usage of the Veolia API"""

import asyncio
import logging

from veolia_api.veolia_api import ConsumptionType, VeoliaAPI

logging.basicConfig(level=logging.DEBUG)


async def main() -> None:
    """Main function."""
    api = VeoliaAPI("username", "password")
    await api.login()

    try:
        ### Get the consumption data for the year 2024
        data = await api.get_consumption_data(ConsumptionType.YEARLY, 2024)
        print(data)

        ### Get the consumption data for Octobre 2024
        data = await api.get_consumption_data(ConsumptionType.MONTHLY, 2024, 10)
        print(data)

        #### Get the alerts set for the account
        # data = await api.get_alerts()

        ### Set the alerts for the account
        # alerts = AlertSettings(
        #     daily_enabled=True,
        #     daily_threshold=550,
        #     daily_contact_email=True,
        #     daily_contact_sms=True,
        #     monthly_enabled=True,
        #     monthly_threshold=8,
        #     monthly_contact_email=True,
        #     monthly_contact_sms=True
        # )
        # data = await api.set_alerts(alerts)
        # print(data)
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
