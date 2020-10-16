import config

guide = {
    'definition': '*What is smog?*\nSmog is a mixture of carbon monoxide, particulate matter, ground level ozone and oxides of nitrogen and sulfur dioxide. Smog is poisonous ☠ and may create many health hazards',

    'effects': '*How does it affect our body?*\n1. Interferes with the respiratory system.\n2. Aggravates asthma\n3. Lungs can get severely damaged.\n4. Causes irritation in eyes 👀 .\n5. Can cause chronic diseases like emphysema and bronchitis--and can also reduce the body\'s ability to fight infections.\n6. Difficulty in breathing and Shortness of Breath\n7. Nausea 🤢 and Vomiting',

    'sources': '*What are its sources?*\nAutomobile emissions 🚗 , power plants 🏭 , industrial boilers, refineries, chemical plants, cleaning products, paints, varnishes, waxes, pesticides and degreasers.',
    'high_risk': '*Who are at a higher risk?*\nChildren 👶🏻 , elderly 👵🏻 and those with a weak immune system are most likely to be affected by smog.',

    'dos': '`DO`\n1. Consume jaggery and honey 🍯 as they make your immune system rock solid.\n\n2. Have herbal ginger and tulsi tea ☕.\n\n3. Include the following food items in your diet:\n_Vitamin C :_ Strawberries 🍓, Papayas, Guava and [others](https://www.globalhealingcenter.com/natural-health/foods-high-in-vitamin-c/).\n_Magnesium :_ Spinach, Beans, Nuts, Bananas 🍌 and [others](https://www.healthaliciousness.com/articles/foods-high-in-magnesium.php).\n_Omega Fatty Acids :_ Flaxseed, Eggs 🥚 , Soybeans, Walnuts and [others](https://www.webmd.com/diet/guide/your-omega-3-family-shopping-list#1).\n\n4. Keep the body hydrated by drinking more water 💧 than usual during this time.\n\n5. Installing certain indoor plants 🌱 like Snakeplant, Golden Pothos, English Ivy can prove beneficial in eliminating pollutants from the air.\n\n6. Invest in a mask. For more info about masks click /masks.\n\n7. Use public transport 🚍🚋 and carpool 🚗 if possible.\n\n8. If you feel irritation in the throat and nose 👃🏻, take steam ♨️ and do salt water gargles.\n\n9. If possible invest in an air purifier (only with Hepa, carbon and pre filter), and use it especially in the kids 👶🏻 or elderlies 👴🏻 room, or those who have respiratory problems and pregnant ladies.',

    'donts': '`DON\'T`\n1. Avoid morning walks 🚶🏻 as the levels of smog are at their highest during the early hours of the day.\n\n2. _Avoid eating outside :_ Food 🍔 long exposed to air pollution can cause severe illness at this juncture.\n\n3. _Do not wear surgical masks 😷 :_ It is important to be aware of the different types of masks available in the market. Surgical masks are different from pollution masks and do not protect from micro-particles like PM2.5, which happen to be the primary cause of ailments in the human body.\n\n4. _Do not smoke 🚬 :_ As per doctors, inhaling the air at present is equal to smoking 50 cigarettes. Trust us, you do not want to smoke more cigarettes than that.\n\n5. Avoid burning 🔥 anything in open or if someone is doing please raise an alarm.\n\n6. Try to avoid use of incense sticks and swap its use with a ghee lamp.\n\n7. Do not sweep/mop in morning ☀ hours, instead substitute it with wet mopping with warm water and a pinch of baking soda in it.\n\n8. Do not send your kids 👶🏻 (less than 7-year-old) to school if AQI is higher than 350.\n\n9. Avoid walking 🚶🏻 directly on the main road 🛣 as it will lead to higher exposure so better walk on side lanes/footpaths.',

    'measures': 'There are certain dos and don\'ts that will help in reducing the ill effects of smog, click the buttons below!'
}

messages = {
    'welcome_msg': '🤖! I can send you information about the pollution 🏭 levels of your location. Try /help for the list of commands.',
    'location_request_msg': 'Would you mind sharing your location 📍 with me?',
    'high_pollution_msg': 'Looks like the pollution 🏭 levels at your place are not healthy, try /guide for help.',
    'accept_feedback_msg': 'Now send me your message so that I can forward it to my creator.',
    'feedback_sent_msg': 'Feedback Sent!',
    'send_guide_msg': 'I have prepared a small guide 📖, to help you survive through the pollution. Take a look 👀 at it!',
    'masks': 'To know more about masks and which ones to buy, select an option from the menu!',
    'masks_available_msg': '*Some of the best masks available in the market:*\n\n- [3M 9004V Particulate Respirator Mask](https://www.amazon.in/3M-9004V-Particulate-Respirator-White/dp/B0146DEWY6) (#10 for ₹360)\n\n- [Honeywell PM 2.5 Anti-Pollution face mask](https://www.amazon.in/Honeywell-Foldable-Face-Mask-Multicolor/dp/B01AJI0QRO) (#3 for ₹199) : Comes with extra exhalation valve to avoid moisture.\n\n- [Dettol Air Protect mask PM 2.5](https://www.amazon.in/Dettol-Air-Protect-Mask/dp/B01CHNUONA) (₹399): It also protects from pbateria, dust and pollen.\n\n- [Grinhealth Anti-Pollution Mask](https://www.amazon.in/Grin-Health-Anti-Pollution-Mask-P/dp/B01N17EHKJ) (₹599)\n- [Veeon, V Mask N99](https://www.amazon.in/Veeon-presents-Organic-Cotton-Filtering/dp/B01NAIH2LH) (₹805)\n- [Atlanta Healthcare Cambridge N99](https://www.amazon.in/Atlanta-Healthcare-Cambridge-Standard-Pollution/dp/B01KK2NQ4O) (₹1300-2100)\n\n- [Respro Anti Pollution City Mask](https://www.amazon.in/Respro-RP00185-Techno-Anti-Pollution-Extra/dp/B00NBYPJLC) (₹2999): It is designed for prolonged use so that one does not feel suffocated.\n\n- [Oxypure N99 mask](https://www.amazon.in/Oxypure-Tested-Washable-Designer-Pollution/dp/B076HWHDGW) (Currently Unavailable): It has special filters with dust holding capacity for extended life.\n\nWell, if you are a bit fashion conscious and also want to stay protected from the pollution, you can also consider [Vogmask’s N99 mask](https://www.nirvanabeing.com/shop/) (₹1800-2400), which has been designed by Manish Arora.',
    'masks_guide_msg': '*Here are a few points you can keep in mind when buying a mask:*\n\n*Check 1:* When buying a mask, look for their rating – N95, N99, N100, P95 and P100. The ratings classify how much pollutants each of them can filter. An N95 mask would filter 95 per cent of PM2.5 while N99 and N100 are capable of filtering 99 per cent and 99.7 per cent particulate matter. A ‘P’ rated mask signifies that it can also filter out oil-based pollutants.\n\n*Check 2:* Mask should protect you from viruses 👾 , bacteria and VOCs (Volatile Organic Compounds).\n\n*Check 3:* Look out for a mask with good fabric quality & strong nose 👃🏻 bands that are adjustable. A non-adjustable mask may cause pain after prolonged use. A washable mask which has a reusable filter would last longer and is the best bet in the long run.\n\n*Check 4:* Look for masks that also have an exhalation valve. These masks direct the exhaled out through a passage so that there is no suffocation or fogging near the nose-bridge 👃🏻 and eyes 👀.',
    'help_msg': 'I can understand the following commands :\n\n/quality - to check the Air Quality Index of your location\n/search - to check the Air Quality Index of any place\n/guide - to get detailed information about Smog and how to tackle it\n/masks - to find out about various masks you can buy and use\n/feedback - to send feedback to the creator\n/rate - to submit rating to Bot Store',
    'rate_msg': f"Thank you for using me, it would mean a lot to me, if you took a minute to rate me at : {config.rating_link}",
    'privacy_msg': 'A little concerned about your privacy 👁️‍🗨️🔒, no worries, try our search 🔍 feature instead.\n_Usage :_ `/search cityname`',
    'search_fail': 'Sorry 😕, but you didn\'t pass any city\'s name to search for.\n\n_Usage : _\n`/search cityname`',
    'pm25_mask': 'If PM2.5 pollution levels in your city is unhealthy or worse, then please consider investing in face /masks for when you’re outdoors, and an air purifier for your home.',
    'pm10_mask': 'If PM10 pollution levels in your city is unhealthy or worse, then please consider investing face /masks for when you’re outdoors, and an air purifier for your home.',
}

pollutants = {
    'pm25': 'PM2.5 measures air particles that are 2.5 micrometers in diameter and smaller. These tiny particles pose the greatest health problems because they can get deep into your lungs and even into your bloodstream.',
    'pm10': 'PM10 measures air particles that are 10 micrometers in diameter and smaller. These tiny particles pose serious health problems because they can get deep into your lungs and even into your bloodstream.',
    'co': 'The largest source of Carbon Monoxide (CO) is vehicle emissions. Breathing the high concentrations of CO leads to reduced Oxygen transport by hemoglobin and has health effects that include headaches, increased risk of chest pain for persons with heart disease, and impaired reaction timing.',
    'no2': 'Nitrogen Dioxide (NO2) pollutes the air mainly as a result of road traffic and energy production. Long term exposure to Nitrogen Dioxide may decrease lung function and cause other health symptoms too.',
    'so2': 'Sulphur Dioxide (SO2) pollutes the air mainly as a result of coal-fired power plants. Sulphur Dioxide causes nerve stimulation in the lining of the nose and throat, which can cause irritation, coughing and a feeling of chest tightness.',
    'o3': 'Breathing ozone can trigger a variety of health problems, particularly for children, the elderly, and people of all ages who have lung diseases such as asthma.',
}
