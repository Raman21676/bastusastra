# Bastusastra - Astrology Knowledge Base

This document contains all formulas, tables, rules, and algorithms extracted from the three astrology books.

**Sources:**
1. **Predictive Astrology of the Hindus** by Pandit Gopesh Kumar Ojha (358 pages)
2. **Jataka Parijata (Volume 1)** by Vaidyanatha Dikshita (324 pages)
3. **Brihat Jataka (2nd Edition)** by V. Subrahmanya Sastri (scanned, needs OCR)

---

## Table of Contents
1. [Astronomical Foundations](#1-astronomical-foundations)
2. [The Zodiac and Constellations](#2-the-zodiac-and-constellations)
3. [Time Systems](#3-time-systems)
4. [Ascendant (Lagna) Calculation](#4-ascendant-lagna-calculation)
5. [Planetary Data](#5-planetary-data)
6. [Divisional Charts (Vargas)](#6-divisional-charts-vargas)
7. [Dasha Systems](#7-dasha-systems)
8. [Yoga and Dosha Detection](#8-yoga-and-dosha-detection)
9. [Panchang Elements](#9-panchang-elements)
10. [House Significations](#10-house-significations)
11. [Planetary Relationships](#11-planetary-relationships)
12. [Compatibility (Kundali Milan)](#12-compatibility-kundali-milan)

---

## 1. Astronomical Foundations

### 1.1 The Zodiac
**Source:** Predictive Astrology of the Hindus, Chapter 1

The zodiac is a belt of the heavens limited by lines of about 8 degrees from the ecliptic on each side. All planets traverse within this belt.

- **Sun's path**: Along the ecliptic
- **Planetary latitude**: Never exceeds 8° north or south of ecliptic
- **Rahu (North Node)**: Where Moon cuts ecliptic going north
- **Ketu (South Node)**: Where Moon cuts ecliptic going south
- **Rahu and Ketu**: Always 180° apart

### 1.2 Sidereal vs Tropical Zodiac

**Sidereal Zodiac (Nirayana)**: Based on fixed stars
**Tropical Zodiac (Sayana)**: Based on moving equinoxes

**Ayanamsa (Precession)**: The distance between the commencing points of the two zodiacs.
- Current value (as of 1969): approximately 23° 26'
- Rate of precession: approximately 1 degree per 72 years
- Lahiri Ayanamsa is the standard in India

**Formula for Ayanamsa:**
```
Sidereal Longitude = Tropical Longitude - Ayanamsa
```

### 1.3 Julian Day Number
Used for astronomical calculations. Reference epoch: January 1, 4713 BCE at noon UT.

---

## 2. The Zodiac and Constellations

### 2.1 The 27 Nakshatras (Constellations)
**Source:** Predictive Astrology of the Hindus, Chapter 1, Page 5-6

Each Nakshatra has a jurisdiction of **13° 20'** (360° ÷ 27 = 13° 20').

| # | Nakshatra | Sanskrit | Longitude (Sidereal) | Symbol | Stars |
|---|-----------|----------|---------------------|--------|-------|
| 1 | Ashwini | अश्विनी | 0°00' - 13°20' | Face of a horse | 3 |
| 2 | Bharani | भरणी | 13°20' - 26°40' | Yoni | 3 |
| 3 | Krittika | कृत्तिका | 26°40' - 40°00' | Curved knife | 6 |
| 4 | Rohini | रोहिणी | 40°00' - 53°20' | Cart | 5 |
| 5 | Mrigashira | मृगशीर्ष | 53°20' - 66°40' | Face of a deer | 3 |
| 6 | Ardra | आर्द्रा | 66°40' - 80°00' | Jewel | 1 |
| 7 | Punarvasu | पुनर्वसु | 80°00' - 93°20' | House | 4 |
| 8 | Pushya | पुष्य | 93°20' - 106°40' | Arrow | 3 |
| 9 | Ashlesha | आश्लेषा | 106°40' - 120°00' | Circular | 5 |
| 10 | Magha | मघा | 120°00' - 133°20' | House | 5 |
| 11 | Poorvaphalguni | पूर्वाफाल्गुनी | 133°20' - 146°40' | Manchaka | 2 |
| 12 | Uttaraphalguni | उत्तराफाल्गुनी | 146°40' - 160°00' | Small cot | 2 |
| 13 | Hasta | हस्त | 160°00' - 173°20' | Hand | 5 |
| 14 | Chitra | चित्रा | 173°20' - 186°40' | Pearl | 1 |
| 15 | Swati | स्वाती | 186°40' - 200°00' | Coral | 1 |
| 16 | Vishakha | विशाखा | 200°00' - 213°20' | Torana | 4 |
| 17 | Anuradha | अनुराधा | 213°20' - 226°40' | Vali | 4 |
| 18 | Jyeshtha | ज्येष्ठा | 226°40' - 240°00' | Circular earring | 4 |
| 19 | Moola | मूला | 240°00' - 253°20' | Tail of a lion | 3 |
| 20 | Poorvashadha | पूर्वाषाढ़ा | 253°20' - 266°40' | Tusk of elephant | 11 |
| 21 | Uttarashadha | उत्तराषाढ़ा | 266°40' - 280°00' | Manchaka | 2 |
| 22 | Shravana | श्रवण | 280°00' - 293°20' | Aeroplane | 3 |
| 23 | Dhanishtha | धनिष्ठा | 293°20' - 306°40' | Mridanga | 4 |
| 24 | Shatabhisha | शतभिषा | 306°40' - 320°00' | Elliptic (100 physicians) | 100 |
| 25 | Poorvabhadra | पूर्वाभाद्रपदा | 320°00' - 333°20' | Manchaka | 2 |
| 26 | Uttarabhadra | उत्तराभाद्रपदा | 333°20' - 346°40' | Small cot | 2 |
| 27 | Revati | रेवती | 346°40' - 360°00' | Drum | 32 |

**Abhijit**: An additional Nakshatra between Uttarashadha and Shravana (not commonly used now).

### 2.2 The 12 Zodiac Signs (Rashis)
**Source:** Jataka Parijata, Adhyaya I

Each Rashi = 30° (360° ÷ 12 = 30°)
Each Rashi contains 2¼ Nakshatras (9 quarters of Nakshatras)

| # | Sign | Sanskrit | Degrees | Element | Quality | Gender | Lord |
|---|------|----------|---------|---------|---------|--------|------|
| 1 | Aries | मेष (Mesha) | 0°-30° | Fire | Movable | Male | Mars |
| 2 | Taurus | वृषभ (Vrishabha) | 30°-60° | Earth | Fixed | Female | Venus |
| 3 | Gemini | मिथुन (Mithuna) | 60°-90° | Air | Dual | Male | Mercury |
| 4 | Cancer | कर्क (Karka) | 90°-120° | Water | Movable | Female | Moon |
| 5 | Leo | सिंह (Simha) | 120°-150° | Fire | Fixed | Male | Sun |
| 6 | Virgo | कन्या (Kanya) | 150°-180° | Earth | Dual | Female | Mercury |
| 7 | Libra | तुला (Thula) | 180°-210° | Air | Movable | Male | Venus |
| 8 | Scorpio | वृश्चिक (Vrischika) | 210°-240° | Water | Fixed | Female | Mars |
| 9 | Sagittarius | धनु (Dhanu) | 240°-270° | Fire | Dual | Male | Jupiter |
| 10 | Capricorn | मकर (Makara) | 270°-300° | Earth | Movable | Female | Saturn |
| 11 | Aquarius | कुंभ (Kumbha) | 300°-330° | Air | Fixed | Male | Saturn |
| 12 | Pisces | मीन (Meena) | 330°-360° | Water | Dual | Female | Jupiter |

### 2.3 Sign Characteristics
**Source:** Jataka Parijata, Sloka 13-25

**Sign Lengths:**
- **Short signs**: Aries, Taurus, Aquarius
- **Even signs**: Gemini, Cancer, Sagittarius, Capricorn, Pisces
- **Long signs**: Scorpio, Virgo, Leo, Libra

**Sign Rising Patterns:**
- **Prishthodaya (rear-first)**: Taurus, Cancer, Sagittarius, Capricorn, Pisces (strong at night)
- **Shirshodaya (head-first)**: Aries, Gemini, Leo, Virgo, Libra, Aquarius (strong during day)
- **Ubhayodaya (both)**: Pisces (when rising as dual fish)

**Sign Types:**
- **Biped (human)**: Gemini, Virgo, Libra, Sagittarius (first half), Aquarius
- **Quadruped**: Aries, Taurus, Leo (first half), Sagittarius (second half), Capricorn (second half)
- **Reptile/Watery**: Cancer, Scorpio, Pisces

**Castes:**
- **Brahmin**: Pisces, Scorpio, Taurus (some texts say Cancer)
- **Kshatriya**: Sagittarius, Aries, Leo
- **Vaishya**: Aquarius, Gemini, Libra
- **Shudra**: Virgo, Capricorn, Cancer

**Elements:**
- **Fire**: Aries, Leo, Sagittarius
- **Earth**: Taurus, Virgo, Capricorn
- **Air**: Gemini, Libra, Aquarius
- **Water**: Cancer, Scorpio, Pisces

---

## 3. Time Systems

### 3.1 Traditional Hindu Time Units
**Source:** Predictive Astrology of the Hindus, Chapter 3, Page 27

```
1 Day & Night = 60 Ghatis
1 Ghati = 60 Palas
1 Pala = 60 Vipalas

Modern Conversion:
1 Ghati = 24 minutes
1 Pala = 24 seconds
1 Vipala = 0.4 seconds
```

### 3.2 The 60-Year Cycle (Samvatsara)
**Source:** Predictive Astrology of the Hindus, Page 19-20

Hindu calendar uses a 60-year cycle with specific names for each year.

### 3.3 The 12 Hindu Months
1. Chaitra
2. Vaishakha
3. Jyeshtha
4. Ashadha
5. Shravana
6. Bhadra
7. Ashwina
8. Kartika
9. Margashirsha
10. Pausha
11. Magha
12. Phalguna

### 3.4 Tithi (Lunar Day) Calculation
**Source:** Predictive Astrology of the Hindus, Page 22-23

Tithi is determined by the angular distance between Sun and Moon.
Each Tithi = 12° of lunar distance.

**Bright Half (Shukla Paksha) - Waxing Moon:**
| Tithi | Distance from Sun |
|-------|-------------------|
| 1 (Pratipat) | 0° - 12° |
| 2 (Dwiteeya) | 12° - 24° |
| 3 (Triteeya) | 24° - 36° |
| ... | ... |
| 14 (Chaturdashi) | 156° - 168° |
| 15 (Poornima) | 168° - 180° |

**Dark Half (Krishna Paksha) - Waning Moon:**
| Tithi | Distance from Sun |
|-------|-------------------|
| 1 (Pratipat) | 180° - 168° |
| ... | ... |
| 14 (Chaturdashi) | 24° - 12° |
| 30 (Amavasya) | 12° - 0° |

**Formula:**
```
Moon Longitude - Sun Longitude = Lunar Distance
If negative, add 360°
Tithi Number = floor(Lunar Distance / 12°) + 1
```

### 3.5 Karana (Half Tithi)
**Source:** Predictive Astrology of the Hindus, Page 24

Each Tithi is divided into 2 Karanas.

**7 Repeating Karanas:**
1. Bava
2. Balava
3. Kaulava
4. Taitila
5. Gara
6. Vanija
7. Vishti (Bhadra)

**4 Special Karanas:**
- Kinstughna (1st half of 1st Tithi in Shukla)
- Shakuni (2nd half of Chaturdashi in Krishna)
- Chatushpada (1st half of Amavasya)
- Naga (2nd half of Amavasya)

### 3.6 Yoga Calculation
**Source:** Predictive Astrology of the Hindus, Page 25-26

Yoga is calculated by adding the longitudes of Sun and Moon.

**Formula:**
```
Yoga Longitude = Sun Longitude + Moon Longitude
If > 360°, subtract 360°
Yoga Number = floor(Yoga Longitude / 13°20') + 1
```

**27 Yogas:**
| # | Yoga | Longitude Range |
|---|------|-----------------|
| 1 | Vishkumbh | 0°00' - 13°20' |
| 2 | Priti | 13°20' - 26°40' |
| 3 | Ayushmana | 26°40' - 40°00' |
| 4 | Saubhagya | 40°00' - 53°20' |
| 5 | Shobhana | 53°20' - 66°40' |
| 6 | Atiganda | 66°40' - 80°00' |
| 7 | Sukarma | 80°00' - 93°20' |
| 8 | Dhriti | 93°20' - 106°40' |
| 9 | Shoola | 106°40' - 120°00' |
| 10 | Ganda | 120°00' - 133°20' |
| 11 | Vriddhi | 133°20' - 146°40' |
| 12 | Dhruva | 146°40' - 160°00' |
| 13 | Vyaghata | 160°00' - 173°20' |
| 14 | Harshana | 173°20' - 186°40' |
| 15 | Vajra | 186°40' - 200°00' |
| 16 | Siddhi | 200°00' - 213°20' |
| 17 | Vyatipata | 213°20' - 226°40' |
| 18 | Variyana | 226°40' - 240°00' |
| 19 | Parigha | 240°00' - 253°20' |
| 20 | Shiva | 253°20' - 266°40' |
| 21 | Siddha | 266°40' - 280°00' |
| 22 | Sadhya | 280°00' - 293°20' |
| 23 | Shubha | 293°20' - 306°40' |
| 24 | Shukla | 306°40' - 320°00' |
| 25 | Brahma | 320°00' - 333°20' |
| 26 | Indra | 333°20' - 346°40' |
| 27 | Vaidhriti | 346°40' - 360°00' |

---

## 4. Ascendant (Lagna) Calculation
**Source:** Predictive Astrology of the Hindus, Chapter 4

### 4.1 Required Data
1. Longitude of birth place
2. Latitude of birth place
3. Date of birth
4. Standard time of birth

### 4.2 Calculation Steps

**Step 1: Convert Standard Time to Local Mean Time (LMT)**
```
Indian Standard Time (IST) is based on 82°30' East longitude.

Formula:
Time Difference = (Birth Longitude - 82°30') × 4 minutes

If Birth Longitude > 82°30': Add the difference
If Birth Longitude < 82°30': Subtract the difference

Example for Delhi (77°13' E):
(77°13' - 82°30') = -5°17'
-5°17' × 4 = -21 minutes 8 seconds
So LMT = IST - 21m 8s
```

**Step 2: Calculate Sidereal Time at Birth**
```
From Ephemeris:
1. Get Sidereal Time at preceding noon (ST)
2. Add time elapsed since noon until birth (in LMT)
3. Add acceleration: 9.856 seconds per hour of elapsed time

Formula:
Sidereal Time = ST at noon + Time since noon + Acceleration

If hours > 24, subtract 24
```

**Step 3: Find Right Ascension of Meridian Cusp (RAMC)**
This is the calculated Sidereal Time.

**Step 4: Use Table of Houses**
- Look up the Table of Houses for the birth latitude
- Find the sign and degree corresponding to the RAMC
- Interpolate if necessary

**Step 5: Apply Ayanamsa (if using Tropical Tables)**
```
Sidereal Ascendant = Tropical Ascendant - Ayanamsa
```

### 4.3 Sunrise/Sunset Corrections
**Source:** Predictive Astrology of the Hindus, Page 36

For accurate sunrise:
- Deduct 3 minutes 25 seconds from visible sunrise
- This accounts for:
  - Refraction: 2 minutes 15 seconds
  - Upper limb to center: 1 minute 10 seconds

### 4.4 Duration of Signs Rising
**At Equator:**
| Sign Group | Duration |
|------------|----------|
| Aries, Virgo, Libra, Pisces | 51 minutes |
| Taurus, Leo, Scorpio, Aquarius | 59 minutes |
| Gemini, Cancer, Sagittarius, Capricorn | 60 minutes |

**At Higher Latitudes:**
- Duration of Aries, Taurus, Gemini decreases
- Duration of Cancer, Leo, Virgo increases correspondingly

---

## 5. Planetary Data

### 5.1 Planetary Lords of Signs
**Source:** Jataka Parijata, Sloka 25

| Planet | Own Signs | Moolatrikona | Exaltation | Debilitation | Exaltation Degree |
|--------|-----------|--------------|------------|--------------|-------------------|
| Sun | Leo | Leo (0°-20°) | Aries | Libra | 10° Aries |
| Moon | Cancer | Taurus (3°-30°) | Taurus | Scorpio | 3° Taurus |
| Mars | Aries, Scorpio | Aries (0°-12°) | Capricorn | Cancer | 28° Capricorn |
| Mercury | Gemini, Virgo | Virgo (15°-20°) | Virgo | Pisces | 15° Virgo |
| Jupiter | Sagittarius, Pisces | Sagittarius (0°-10°) | Cancer | Capricorn | 5° Cancer |
| Venus | Taurus, Libra | Libra (0°-15°) | Pisces | Virgo | 27° Pisces |
| Saturn | Capricorn, Aquarius | Aquarius (0°-20°) | Libra | Aries | 20° Libra |
| Rahu | - | - | Taurus (some texts) | Scorpio | - |
| Ketu | - | - | Scorpio (some texts) | Taurus | - |

### 5.2 Planetary Relationships
**Source:** Predictive Astrology of the Hindus, Chapter 6

**Natural Friendship/Enmity:**
| Planet | Friends | Enemies | Neutral |
|--------|---------|---------|---------|
| Sun | Moon, Mars, Jupiter | Venus, Saturn | Mercury |
| Moon | Sun, Mercury | - | Mars, Jupiter, Venus, Saturn |
| Mars | Sun, Moon, Jupiter | Mercury | Venus, Saturn |
| Mercury | Sun, Venus | Moon | Mars, Jupiter, Saturn |
| Jupiter | Sun, Moon, Mars | Mercury, Venus | Saturn |
| Venus | Mercury, Saturn | Sun, Moon | Mars, Jupiter |
| Saturn | Mercury, Venus | Sun, Moon, Mars | Jupiter |

**Temporary Relationships:**
Planets in 2nd, 3rd, 4th, 10th, 11th, 12th from a planet are temporal friends.
Planets in 1st (same), 5th, 6th, 7th, 8th, 9th are temporal enemies.

**Resultant Relationship:**
- Natural friend + Temporal friend = Great Friend
- Natural friend + Temporal enemy = Neutral
- Natural enemy + Temporal friend = Neutral
- Natural enemy + Temporal enemy = Great Enemy

### 5.3 Planetary Aspects
**Source:** Jataka Parijata

| Planet | Aspects |
|--------|---------|
| Sun | 7th |
| Moon | 7th |
| Mars | 4th, 7th, 8th |
| Mercury | 7th |
| Jupiter | 5th, 7th, 9th |
| Venus | 7th |
| Saturn | 3rd, 7th, 10th |
| Rahu | 5th, 7th, 9th, 12th |
| Ketu | 5th, 7th, 9th, 12th |

### 5.4 Planetary Characteristics
**Source:** Predictive Astriology of the Hindus, Chapter 6

| Attribute | Sun | Moon | Mars | Mercury | Jupiter | Venus | Saturn |
|-----------|-----|------|------|---------|---------|-------|--------|
| Element | Fire | Water | Fire | Earth | Ether | Water | Air |
| Gender | Male | Female | Male | Neutral | Male | Female | Neutral |
| Caste | Kshatriya | Vaishya | Kshatriya | Vaishya | Brahmin | Brahmin | Shudra |
| Guna | Sattva | Sattva | Tamas | Rajas | Sattva | Rajas | Tamas |
| Color | Copper | White | Red | Green | Yellow | Variegated | Black |
| Metal | Copper | Silver | Copper | Brass | Gold | Silver | Iron |
| Gem | Ruby | Pearl | Coral | Emerald | Yellow Sapphire | Diamond | Blue Sapphire |
| Direction | East | North-West | South | North | East | South-East | West |
| Day | Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |

---

## 6. Divisional Charts (Vargas)
**Source:** Jataka Parijata, Adhyaya I, Sloka 29-48

### 6.1 The 16 Divisional Charts (Shodashavarga)

| # | Varga | Division | Size | Primary Use |
|---|-------|----------|------|-------------|
| 1 | Rasi | 1/1 | 30° | Body, general life |
| 2 | Hora | 1/2 | 15° | Wealth, prosperity |
| 3 | Drekkana | 1/3 | 10° | Siblings, courage |
| 4 | Chaturthamsa | 1/4 | 7°30' | Fortune, property |
| 5 | Saptamamsa | 1/7 | 4°17' | Children, progeny |
| 6 | Navamsa | 1/9 | 3°20' | Marriage, dharma |
| 7 | Dasamamsa | 1/10 | 3° | Career, status |
| 8 | Dwadasamsa | 1/12 | 2°30' | Parents, lineage |
| 9 | Shodasamsa | 1/16 | 1°52'30" | Vehicles, comforts |
| 10 | Vimsamsa | 1/20 | 1°30' | Spiritual progress |
| 11 | Chaturvimsamsa | 1/24 | 1°15' | Education, learning |
| 12 | Bhamsa/Saptavimsamsa | 1/27 | 1°6'40" | Strength, weakness |
| 13 | Trimsamsa | 1/30 | 1° | Misfortunes, evils |
| 14 | Khavedamsa | 1/40 | 45' | Auspicious results |
| 15 | Akshavedamsa | 1/45 | 40' | General indications |
| 16 | Shashtyamsa | 1/60 | 30' | All general effects |

### 6.2 Hora (D-2) Calculation
**Source:** Jataka Parijata, Sloka 30

**Odd Signs (Aries, Gemini, Leo, Libra, Sagittarius, Aquarius):**
- 0°-15°: Sun Hora
- 15°-30°: Moon Hora

**Even Signs (Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces):**
- 0°-15°: Moon Hora
- 15°-30°: Sun Hora

### 6.3 Drekkana (D-3) Calculation
**Source:** Jataka Parijata, Sloka 30

Each sign divided into 3 parts of 10° each.
Count from the sign itself for odd signs.
Count from 9th sign for even signs.

### 6.4 Navamsa (D-9) Calculation
**Source:** Jataka Parijata, Sloka 32-34

**Formula:**
```
For Odd Signs (Aries, Gemini, Leo, Libra, Sagittarius, Aquarius):
  Navamsa Sign = Starting from same sign
  
For Even Signs (Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces):
  Navamsa Sign = Starting from 9th sign

Each Navamsa = 3°20'
Navamsa Number = floor(degree / 3.333...) + 1
```

**Vargottama Navamsa:**
- 1st Navamsa of movable signs
- 5th Navamsa of fixed signs
- 9th Navamsa of dual signs

When a planet occupies the same sign in Rasi and Navamsa, it is Vargottama.

### 6.5 Dasamamsa (D-10) Calculation
**Source:** Jataka Parijata, Sloka 35

- **Odd signs**: Count from the sign itself
- **Even signs**: Count from the 9th sign

Each Dasamamsa = 3°

### 6.6 Dwadasamsa (D-12) Calculation
**Source:** Jataka Parijata, Sloka 35

Each sign divided into 12 parts of 2°30' each.
Count from the sign itself.

### 6.7 Shodasamsa (D-16) Calculation
**Source:** Jataka Parijata, Sloka 36

- **Odd signs**: Count forwards from the sign
- **Even signs**: Count backwards from the sign

Each Shodasamsa = 1°52'30"

### 6.8 Trimsamsa (D-30) Calculation
**Source:** Jataka Parijata, Sloka 37-38

**For Odd Signs:**
| Degrees | Lord |
|---------|------|
| 0°-5° | Mars |
| 5°-10° | Saturn |
| 10°-18° | Jupiter |
| 18°-25° | Mercury |
| 25°-30° | Venus |

**For Even Signs:**
| Degrees | Lord |
|---------|------|
| 0°-5° | Venus |
| 5°-12° | Mercury |
| 12°-20° | Jupiter |
| 20°-25° | Saturn |
| 25°-30° | Mars |

### 6.9 Shashtyamsa (D-60) Calculation
**Source:** Jataka Parijata, Sloka 39-43

**For Odd Signs:** Count forward from the sign
**For Even Signs:** Count backward from the sign

Each Shashtyamsa = 30' (half degree)

| # | Name (Odd) | Name (Even) |
|---|------------|-------------|
| 1 | Ghoramsa | Prabhamsa |
| 2 | Rakshasamsa | Indurekha |
| 3 | Devamsa | Brahmi |
| ... | ... | ... |
| 60 | Indurekha | Ghoramsa |

---

## 7. Dasha Systems

### 7.1 Vimshottari Dasha
**Source:** Predictive Astrology of the Hindus, Chapter 14

Most widely used Dasha system. Total cycle = 120 years.

| Planet | Years | Nakshatras |
|--------|-------|------------|
| Ketu | 7 | Ashwini, Magha, Moola |
| Venus | 20 | Bharani, Purvaphalguni, Purvashadha |
| Sun | 6 | Krittika, Uttaraphalguni, Uttarashadha |
| Moon | 10 | Rohini, Hasta, Shravana |
| Mars | 7 | Mrigashira, Chitra, Dhanishtha |
| Rahu | 18 | Ardra, Swati, Shatabhisha |
| Jupiter | 16 | Punarvasu, Vishakha, Purvabhadra |
| Saturn | 19 | Pushya, Anuradha, Uttarabhadra |
| Mercury | 17 | Ashlesha, Jyeshtha, Revati |

### 7.2 Dasha Balance at Birth Calculation
**Formula:**
```
1. Find Moon's Nakshatra at birth
2. Determine how much of the Nakshatra has elapsed
3. Calculate remaining portion
4. Apply proportion to the Dasha years

Remaining Dashas = (Remaining portion / Total Nakshatra) × Planet's Years
```

### 7.3 Antardasha (Sub-periods)
**Source:** Predictive Astrology of the Hindus, Chapter 15

Within each Mahadasha, planets rule sub-periods.

**Order:** Same as Vimshottari sequence starting from the Mahadasha lord.

**Formula for Antardasha Duration:**
```
Antardasha Years = (Planet's Years × Mahadasha Lord's Years) / 120
```

### 7.4 Pratyantardasha (Sub-sub-periods)
```
Pratyantardasha = (Planet's Years × Antardasha Lord's Years × Mahadasha Lord's Years) / 120²
```

---

## 8. Yoga and Dosha Detection

### 8.1 Major Yogas
**Source:** Jataka Parijata, Adhyaya VII-VIII

**Raj Yoga Formations:**
- Lords of Kendra (1,4,7,10) and Trikona (1,5,9) in mutual association
- Exchange of houses between Kendra and Trikona lords
- Planets in own sign, exaltation, or Moolatrikona
- Vargottama positions

**Dhana Yoga (Wealth):**
- Association of 2nd and 11th lords
- Placement of wealth-giving planets in 2nd or 11th

**Gaja Kesari Yoga:**
- Jupiter and Moon in Kendra from each other
- Both should be strong

### 8.2 Major Doshas

**Mangal Dosha (Manglik):**
Mars in 1st, 2nd, 4th, 7th, 8th, or 12th from Lagna
Exception: If Mars is in its own sign or exaltation in these houses

**Kaal Sarp Dosha:**
All planets between Rahu and Ketu (one-sided placement)

**Sade Sati:**
Transit of Saturn over:
1. Natal Moon sign
2. 12th from Moon
3. 2nd from Moon

---

## 9. Panchang Elements

### 9.1 Daily Panchang Components
1. **Tithi** (Lunar day)
2. **Vara** (Day of week)
3. **Nakshatra** (Lunar mansion)
4. **Yoga** (Sun-Moon combination)
5. **Karana** (Half Tithi)

### 9.2 Inauspicious Times

**Rahu Kaal:**
- 1.5 hours each day
- Sequence: Sun-Mon-Tue-Wed-Thu-Fri-Sat
- Times vary by day of week

**Yamaganda:**
- Similar calculation to Rahu Kaal

**Gulika:**
- Divides day into 8 parts starting from Saturday

---

## 10. House Significations
**Source:** Jataka Parijata, Adhyaya I, Sloka 49-54

| House | Names | Significations |
|-------|-------|----------------|
| 1 | Lagna, Udaya, Tanu | Body, appearance, personality, longevity |
| 2 | Dhana, Kutumba, Vak | Wealth, family, speech, food |
| 3 | Sahaja, Vikrama, Parakrama | Siblings, courage, communication, short travels |
| 4 | Bandhu, Griha, Sukha | Mother, home, vehicles, happiness, education |
| 5 | Putra, Buddhi, Dhi | Children, intelligence, speculation, mantras |
| 6 | Ripu, Shatru, Roga | Enemies, diseases, debts, obstacles, service |
| 7 | Kalatra, Jamitra, Dyuna | Marriage, partnerships, foreign lands |
| 8 | Ayur, Randhra, Mrityu | Longevity, sudden events, occult, inheritance |
| 9 | Dharma, Bhagya, Pitri | Fortune, father, religion, higher learning, travel |
| 10 | Karma, Meshurana, Rajya | Career, status, honor, government |
| 11 | Labha, Upabhoga | Gains, income, friends, elder siblings |
| 12 | Vyaya, Anthya, Ripha | Expenses, losses, liberation, foreign residence |

### 10.1 House Classifications

**Kendra (Angular Houses):** 1st, 4th, 7th, 10th
**Trikona (Trinal Houses):** 1st, 5th, 9th
**Upachaya (Growth Houses):** 3rd, 6th, 10th, 11th
**Panaphara (Succedent):** 2nd, 5th, 8th, 11th
**Apoklima (Cadent):** 3rd, 6th, 9th, 12th
**Maraka (Death-inflicting):** 2nd, 7th
**Dusthana (Evil Houses):** 6th, 8th, 12th

---

## 11. Planetary Relationships

### 11.1 Natural (Naisargika) Relationships
**Source:** Jataka Parijata, Adhyaya II

**Friends:**
- Sun: Moon, Mars, Jupiter
- Moon: Sun, Mercury
- Mars: Sun, Moon, Jupiter
- Mercury: Sun, Venus
- Jupiter: Sun, Moon, Mars
- Venus: Mercury, Saturn
- Saturn: Mercury, Venus

**Enemies:**
- Sun: Venus, Saturn
- Moon: None specifically
- Mars: Mercury
- Mercury: Moon
- Jupiter: Mercury, Venus
- Venus: Sun, Moon
- Saturn: Sun, Moon, Mars

### 11.2 Temporary (Tatkalika) Relationships
Planets in houses 3, 10, 11, 12 from a planet are temporary friends.
Planets in houses 1, 2, 4, 5, 6, 7, 8, 9 are temporary enemies.

### 11.3 Combined (Panchadha) Relationships

| Natural | Temporary | Result |
|---------|-----------|--------|
| Friend | Friend | Great Friend (Adhimitra) |
| Friend | Enemy | Neutral (Sama) |
| Enemy | Friend | Neutral (Sama) |
| Enemy | Enemy | Great Enemy (Adhisatru) |
| Neutral | Friend | Friend (Mitra) |
| Neutral | Enemy | Enemy (Satru) |

---

## 12. Compatibility (Kundali Milan)

### 12.1 Ashta Koota (8-Fold Matching)
Total Points: 36

| Koota | Points | Factors |
|-------|--------|---------|
| Varna | 1 | Caste compatibility |
| Vashya | 2 | Mutual attraction |
| Tara | 3 | Birth star compatibility |
| Yoni | 4 | Sexual compatibility |
| Graha Maitri | 5 | Planetary friendship |
| Gana | 6 | Temperament matching |
| Bhakoot | 7 | Relative position of Moons |
| Nadi | 8 | Health compatibility |

### 12.2 Gana Matching
**Deva Gana:** Ashwini, Mrigashira, Punarvasu, Pushya, Hasta, Swati, Anuradha, Sravana, Revati
**Manushya Gana:** Bharani, Rohini, Ardra, Purvaphalguni, Purvashadha, Purvabhadra
**Rakshasa Gana:** Krittika, Ashlesha, Magha, Chitra, Vishakha, Jyeshtha, Moola, Dhanishtha, Shatabhisha, Uttarabhadra

**Matching:**
- Deva + Deva = Good
- Deva + Manushya = Good
- Manushya + Manushya = Good
- Rakshasa + Rakshasa = Good
- Deva + Rakshasa = Bad
- Manushya + Rakshasa = Bad

### 12.3 Nadi Matching
| Nakshatra | Nadi |
|-----------|------|
| Ashwini, Ardra, Punarvasu, Uttara, Hasta, Jyeshtha, Moola, Shatabhisha, Purvabhadra | Adi |
| Bharani, Mrigashira, Pushya, Purvaphalguni, Chitra, Anuradha, Purvashadha, Dhanishtha, Uttarabhadra | Madhya |
| Krittika, Rohini, Ashlesha, Magha, Swati, Vishakha, Uttarashadha, Shravana, Revati | Antya |

**Rule:** Same Nadi = 0 points (avoid marriage)

---

## Gaps Identified in Books

1. **Brihat Jataka**: Needs OCR extraction (scanned PDF)
2. **Advanced Calculations**: Detailed ephemeris calculations not fully covered
3. **Modern Ayanamsa**: Need up-to-date Lahiri ayanamsa values
4. **Planetary Positions**: Need VSOP87 or similar algorithms for precise positions
5. **House Division Systems**: Multiple systems (Placidus, Equal, etc.) need implementation
6. **Muhurta Detailed Rules**: Specific calculations for marriage muhurta need expansion
7. **Gochara (Transit)**: Detailed transit effects need compilation

---

*Document Version: 1.0*
*Created: March 2026*
*Next Update: After Brihat Jataka OCR extraction*
