# Bastusastra - Algorithms Documentation

This document contains pseudo-code for all astrological calculations needed for the website.

---

## Table of Contents
1. [Date/Time Conversions](#1-datetime-conversions)
2. [Ayanamsa Calculation](#2-ayanamsa-calculation)
3. [Planetary Position Calculations](#3-planetary-position-calculations)
4. [Ascendant (Lagna) Calculation](#4-ascendant-lagna-calculation)
5. [House Calculations](#5-house-calculations)
6. [Nakshatra Calculation](#6-nakshatra-calculation)
7. [Tithi Calculation](#7-tithi-calculation)
8. [Yoga Calculation](#8-yoga-calculation)
9. [Karana Calculation](#9-karana-calculation)
10. [Divisional Charts (Vargas)](#10-divisional-charts-vargas)
11. [Dasha Calculations](#11-dasha-calculations)
12. [Yoga Detection](#12-yoga-detection)
13. [Dosha Detection](#13-dosha-detection)
14. [Panchang Generation](#14-panchang-generation)
15. [Compatibility Matching](#15-compatibility-matching)

---

## 1. Date/Time Conversions

### 1.1 Julian Day Number (JDN)
```
FUNCTION calculateJDN(year, month, day, hour, minute, second):
    
    IF month <= 2:
        year = year - 1
        month = month + 12
    
    A = floor(year / 100)
    B = 2 - A + floor(A / 4)
    
    // Julian Day at noon UT
    JD = floor(365.25 * (year + 4716)) + 
         floor(30.6001 * (month + 1)) + 
         day + B - 1524.5
    
    // Add time fraction
    timeFraction = (hour + minute/60 + second/3600) / 24
    
    RETURN JD + timeFraction
END FUNCTION
```

### 1.2 Standard Time to Local Mean Time
```
FUNCTION convertToLMT(standardTime, birthLongitude, standardMeridian):
    // standardMeridian: e.g., 82.5 for IST
    
    longitudeDifference = birthLongitude - standardMeridian
    timeDifferenceMinutes = longitudeDifference * 4  // 4 minutes per degree
    
    lmt = standardTime + timeDifferenceMinutes minutes
    
    RETURN lmt
END FUNCTION
```

### 1.3 Local Mean Time to Sidereal Time
```
FUNCTION calculateSiderealTime(jd, longitude):
    
    // Julian centuries from J2000.0
    T = (jd - 2451545.0) / 36525.0
    
    // Mean sidereal time at Greenwich (in degrees)
    GMST = 280.46061837 + 
           360.98564736629 * (jd - 2451545.0) + 
           0.000387933 * T^2 - 
           T^3 / 38710000.0
    
    // Modulo 360
    GMST = GMST mod 360
    
    // Local sidereal time
    LST = GMST + longitude
    LST = LST mod 360
    
    // Convert to hours
    LST_hours = LST / 15
    
    RETURN LST_hours
END FUNCTION
```

---

## 2. Ayanamsa Calculation

### 2.1 Lahiri Ayanamsa
```
FUNCTION calculateLahiriAyanamsa(julianDay):
    
    // Julian centuries from J2000.0
    T = (julianDay - 2451545.0) / 36525.0
    
    // Lahiri ayanamsa formula (simplified)
    // Precession rate: ~50.29 arcseconds per year
    ayanamsa = 23.85 + (T * 50.29 / 3600)
    
    // More precise formula
    // ayanamsa = 23.8565 + T * 0.013971 + T^2 * 0.0000057
    
    RETURN ayanamsa  // in degrees
END FUNCTION

FUNCTION tropicalToSidereal(tropicalLongitude, ayanamsa):
    siderealLongitude = tropicalLongitude - ayanamsa
    IF siderealLongitude < 0:
        siderealLongitude = siderealLongitude + 360
    RETURN siderealLongitude
END FUNCTION
```

---

## 3. Planetary Position Calculations

### 3.1 Sun Position (Simplified)
```
FUNCTION calculateSunLongitude(julianDay):
    
    // Days from J2000.0
    n = julianDay - 2451545.0
    
    // Mean longitude
    L = (280.460 + 0.9856474 * n) mod 360
    
    // Mean anomaly
    g = (357.528 + 0.9856003 * n) mod 360
    g_rad = toRadians(g)
    
    // Ecliptic longitude
    sunLong = L + 1.915 * sin(g_rad) + 0.020 * sin(2 * g_rad)
    sunLong = sunLong mod 360
    
    RETURN sunLong
END FUNCTION
```

### 3.2 Moon Position (Simplified)
```
FUNCTION calculateMoonLongitude(julianDay):
    
    // Days from J2000.0
    d = julianDay - 2451545.0
    
    // Mean longitude
    L = (218.316 + 13.176396 * d) mod 360
    
    // Mean anomaly
    M = (134.963 + 13.064993 * d) mod 360
    
    // Mean elongation
    D = (297.850 + 12.190749 * d) mod 360
    
    // Argument of latitude
    F = (93.272 + 13.229350 * d) mod 360
    
    // Convert to radians
    Lr = toRadians(L)
    Mr = toRadians(M)
    Dr = toRadians(D)
    Fr = toRadians(F)
    
    // Corrections
    moonLong = L + 
               6.289 * sin(Mr) +
               1.274 * sin(2*Dr - Mr) +
               0.658 * sin(2*Dr) +
               0.214 * sin(2*Mr) -
               0.186 * sin(Mr) -
               0.114 * sin(2*Fr)
    
    moonLong = moonLong mod 360
    
    RETURN moonLong
END FUNCTION
```

### 3.3 Rahu/Ketu Calculation
```
FUNCTION calculateRahuLongitude(julianDay):
    
    // Mean ascending node
    // Days from J2000.0
    d = julianDay - 2451545.0
    
    // Mean longitude of node
    omega = (125.044 - 0.0529539 * d) mod 360
    
    RETURN omega
END FUNCTION

FUNCTION calculateKetuLongitude(rahuLongitude):
    ketuLongitude = (rahuLongitude + 180) mod 360
    RETURN ketuLongitude
END FUNCTION
```

### 3.4 Planetary Positions from Ephemeris
```
FUNCTION getPlanetPosition(planet, julianDay, ephemerisData):
    
    // For precise calculations, use Swiss Ephemeris or similar
    // This is a placeholder for ephemeris lookup
    
    planetData = ephemerisData.get(planet, julianDay)
    
    RETURN {
        longitude: planetData.longitude,
        latitude: planetData.latitude,
        distance: planetData.distance,
        speed: planetData.speed
    }
END FUNCTION
```

---

## 4. Ascendant (Lagna) Calculation

### 4.1 Calculate Ascendant
```
FUNCTION calculateAscendant(julianDay, latitude, longitude):
    
    // Get Local Sidereal Time
    lst = calculateSiderealTime(julianDay, longitude)
    lst_degrees = lst * 15  // Convert hours to degrees
    
    // Obliquity of ecliptic
    epsilon = 23.4367  // degrees
    epsilon_rad = toRadians(epsilon)
    
    // Latitude in radians
    lat_rad = toRadians(latitude)
    
    // Calculate ascendant
    // RAMC = Right Ascension of Midheaven (Meridian Cusp)
    ramc = lst_degrees
    
    // Formula for ascendant
    tanA = cos(epsilon_rad) * sin(ramc) / 
           (cos(ramc) * cos(lat_rad) + sin(epsilon_rad) * sin(lat_rad) * sin(ramc))
    
    ascendant = arctan(tanA)
    
    // Convert to degrees and normalize
    ascendant = toDegrees(ascendant)
    ascendant = ascendant mod 360
    
    // Determine quadrant
    IF sin(ramc) < 0:
        ascendant = ascendant + 180
    ELSE IF tanA < 0:
        ascendant = ascendant + 360
    
    // Apply ayanamsa to get sidereal ascendant
    ayanamsa = calculateLahiriAyanamsa(julianDay)
    siderealAscendant = (ascendant - ayanamsa) mod 360
    
    RETURN siderealAscendant
END FUNCTION
```

### 4.2 Calculate All Houses (Equal House System)
```
FUNCTION calculateEqualHouses(ascendantLongitude):
    
    houses = []
    
    FOR houseNumber FROM 1 TO 12:
        houseCusp = (ascendantLongitude + (houseNumber - 1) * 30) mod 360
        houses[houseNumber] = houseCusp
    END FOR
    
    RETURN houses
END FUNCTION
```

### 4.3 Calculate All Houses (Placidus System)
```
FUNCTION calculatePlacidusHouses(lst, latitude, julianDay):
    
    houses = []
    
    // Ascendant (House 1)
    houses[1] = calculateAscendant(julianDay, latitude, lst_to_longitude(lst))
    
    // Midheaven (House 10 cusp)
    houses[10] = calculateMC(lst, julianDay)
    
    // Other houses require iterative calculation
    // This is simplified - full implementation needs house tables
    
    // Calculate semi-arcs for each sign
    FOR houseNumber IN [11, 12, 2, 3]:
        houses[houseNumber] = interpolateHouse(houses[10], houses[1], houseNumber)
    END FOR
    
    // Opposite houses
    FOR houseNumber FROM 4 TO 9:
        houses[houseNumber] = (houses[houseNumber - 6] + 180) mod 360
    END FOR
    
    RETURN houses
END FUNCTION
```

---

## 5. House Calculations

### 5.1 House Lords
```
FUNCTION getHouseLord(houseNumber, ascendantSign):
    
    houseSign = (ascendantSign + houseNumber - 1) mod 12
    IF houseSign == 0:
        houseSign = 12
    
    lord = getSignLord(houseSign)
    
    RETURN lord
END FUNCTION

FUNCTION getSignLord(signNumber):
    lords = {
        1: "Mars",      // Aries
        2: "Venus",     // Taurus
        3: "Mercury",   // Gemini
        4: "Moon",      // Cancer
        5: "Sun",       // Leo
        6: "Mercury",   // Virgo
        7: "Venus",     // Libra
        8: "Mars",      // Scorpio
        9: "Jupiter",   // Sagittarius
        10: "Saturn",   // Capricorn
        11: "Saturn",   // Aquarius
        12: "Jupiter"   // Pisces
    }
    RETURN lords[signNumber]
END FUNCTION
```

### 5.2 House Strength
```
FUNCTION calculateHouseStrength(houseNumber, planetPositions, houses):
    
    houseSign = getHouseSign(houseNumber, houses)
    lord = getSignLord(houseSign)
    
    strength = 0
    
    // Check if lord is in own house
    IF planetPositions[lord].sign == houseSign:
        strength += 10
    
    // Check if lord is exalted
    IF isExalted(lord, planetPositions[lord].sign):
        strength += 10
    
    // Check aspects
    FOR each planet IN planetPositions:
        IF aspectsPlanet(planet, houseSign):
            IF isBenefic(planet):
                strength += 5
            ELSE:
                strength -= 3
    END FOR
    
    RETURN strength
END FUNCTION
```

---

## 6. Nakshatra Calculation

### 6.1 Find Nakshatra
```
FUNCTION findNakshatra(moonLongitude):
    
    // Each nakshatra is 13°20' = 13.333... degrees
    nakshatraSpan = 13 + 20/60  // 13.3333 degrees
    
    // Calculate nakshatra number (0-26)
    nakshatraNumber = floor(moonLongitude / nakshatraSpan)
    
    // Calculate pada (quarter) within nakshatra
    remainder = moonLongitude mod nakshatraSpan
    pada = floor(remainder / (nakshatraSpan / 4)) + 1  // 1-4
    
    // Calculate exact degrees in nakshatra
    degreesInNakshatra = remainder
    
    nakshatras = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
        "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
        "Purvaphalguni", "Uttaraphalguni", "Hasta", "Chitra", "Swati",
        "Vishakha", "Anuradha", "Jyeshtha", "Moola", "Purvashadha",
        "Uttarashadha", "Shravana", "Dhanishtha", "Shatabhisha",
        "Purvabhadra", "Uttarabhadra", "Revati"
    ]
    
    RETURN {
        name: nakshatras[nakshatraNumber],
        number: nakshatraNumber + 1,
        pada: pada,
        degreesInNakshatra: degreesInNakshatra
    }
END FUNCTION
```

### 6.2 Nakshatra Lord
```
FUNCTION getNakshatraLord(nakshatraNumber):
    
    // Vimshottari dasha sequence
    lords = [
        "Ketu",     // 1. Ashwini
        "Venus",    // 2. Bharani
        "Sun",      // 3. Krittika
        "Moon",     // 4. Rohini
        "Mars",     // 5. Mrigashira
        "Rahu",     // 6. Ardra
        "Jupiter",  // 7. Punarvasu
        "Saturn",   // 8. Pushya
        "Mercury",  // 9. Ashlesha
        "Ketu",     // 10. Magha
        "Venus",    // 11. Purvaphalguni
        "Sun",      // 12. Uttaraphalguni
        "Moon",     // 13. Hasta
        "Mars",     // 14. Chitra
        "Rahu",     // 15. Swati
        "Jupiter",  // 16. Vishakha
        "Saturn",   // 17. Anuradha
        "Mercury",  // 18. Jyeshtha
        "Ketu",     // 19. Moola
        "Venus",    // 20. Purvashadha
        "Sun",      // 21. Uttarashadha
        "Moon",     // 22. Shravana
        "Mars",     // 23. Dhanishtha
        "Rahu",     // 24. Shatabhisha
        "Jupiter",  // 25. Purvabhadra
        "Saturn",   // 26. Uttarabhadra
        "Mercury"   // 27. Revati
    ]
    
    RETURN lords[nakshatraNumber - 1]
END FUNCTION
```

---

## 7. Tithi Calculation

### 7.1 Calculate Tithi
```
FUNCTION calculateTithi(sunLongitude, moonLongitude):
    
    // Calculate angular distance
    lunarDistance = moonLongitude - sunLongitude
    
    IF lunarDistance < 0:
        lunarDistance = lunarDistance + 360
    END IF
    
    // Each tithi is 12 degrees
    tithiNumber = floor(lunarDistance / 12) + 1  // 1-30
    
    // Calculate fraction within tithi
    remainder = lunarDistance mod 12
    fraction = remainder / 12
    
    // Determine paksha
    IF tithiNumber <= 15:
        paksha = "Shukla"  // Bright half, waxing
    ELSE:
        paksha = "Krishna"  // Dark half, waning
    END IF
    
    // Tithi name
    tithiNames = [
        "Pratipat", "Dwiteeya", "Triteeya", "Chaturthi", "Panchami",
        "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
        "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
        "Pratipat", "Dwiteeya", "Triteeya", "Chaturthi", "Panchami",
        "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
        "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
    ]
    
    RETURN {
        number: tithiNumber,
        name: tithiNames[tithiNumber - 1],
        paksha: paksha,
        fraction: fraction,
        lunarDistance: lunarDistance
    }
END FUNCTION
```

---

## 8. Yoga Calculation

### 8.1 Calculate Yoga
```
FUNCTION calculateYoga(sunLongitude, moonLongitude):
    
    // Add sun and moon longitudes
    yogaLongitude = (sunLongitude + moonLongitude) mod 360
    
    // Each yoga is 13°20' = 13.333... degrees
    yogaSpan = 13 + 20/60
    
    // Calculate yoga number (1-27)
    yogaNumber = floor(yogaLongitude / yogaSpan) + 1
    
    // Fraction within yoga
    fraction = (yogaLongitude mod yogaSpan) / yogaSpan
    
    yogaNames = [
        "Vishkumbh", "Priti", "Ayushmana", "Saubhagya", "Shobhana",
        "Atiganda", "Sukarma", "Dhriti", "Shoola", "Ganda",
        "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
        "Siddhi", "Vyatipata", "Variyana", "Parigha", "Shiva",
        "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
        "Indra", "Vaidhriti"
    ]
    
    RETURN {
        number: yogaNumber,
        name: yogaNames[yogaNumber - 1],
        longitude: yogaLongitude,
        fraction: fraction
    }
END FUNCTION
```

---

## 9. Karana Calculation

### 9.1 Calculate Karana
```
FUNCTION calculateKarana(tithiNumber, fraction):
    
    // 7 repeating karanas
    repeatingKaranas = [
        "Bava", "Balava", "Kaulava", "Taitila",
        "Gara", "Vanija", "Vishti"
    ]
    
    // Special karanas
    IF tithiNumber == 1 AND fraction < 0.5:
        RETURN "Kinstughna"
    ELSE IF tithiNumber == 30 AND fraction < 0.5:
        RETURN "Chatushpada"
    ELSE IF tithiNumber == 30 AND fraction >= 0.5:
        RETURN "Naga"
    ELSE IF tithiNumber == 14 AND fraction >= 0.5:
        RETURN "Shakuni"
    END IF
    
    // Calculate position in cycle
    // Each tithi has 2 karanas
    totalKaranas = (tithiNumber - 1) * 2
    IF fraction >= 0.5:
        totalKaranas = totalKaranas + 1
    END IF
    
    // Adjust for special karanas at beginning
    totalKaranas = totalKaranas - 1
    
    // Get karana from repeating cycle
    karanaIndex = totalKaranas mod 7
    
    RETURN repeatingKaranas[karanaIndex]
END FUNCTION
```

---

## 10. Divisional Charts (Vargas)

### 10.1 Calculate Navamsa (D-9)
```
FUNCTION calculateNavamsa(planetLongitude, signNumber):
    
    // Get degrees within sign
    degreesInSign = planetLongitude mod 30
    
    // Calculate navamsa number (1-9)
    navamsaSize = 30 / 9  // 3.333... degrees
    navamsaNumber = floor(degreesInSign / navamsaSize) + 1
    
    // Determine starting sign for navamsa count
    IF signNumber IN [1, 3, 5, 7, 9, 11]:  // Odd signs
        startSign = signNumber
    ELSE:  // Even signs
        startSign = ((signNumber + 8) mod 12)
        IF startSign == 0:
            startSign = 12
    END IF
    
    // Calculate navamsa sign
    navamsaSign = ((startSign + navamsaNumber - 2) mod 12) + 1
    
    // Check for Vargottama
    isVargottama = (navamsaSign == signNumber)
    
    RETURN {
        sign: navamsaSign,
        number: navamsaNumber,
        isVargottama: isVargottama
    }
END FUNCTION
```

### 10.2 Calculate Hora (D-2)
```
FUNCTION calculateHora(planetLongitude, signNumber):
    
    degreesInSign = planetLongitude mod 30
    
    IF signNumber IN [1, 3, 5, 7, 9, 11]:  // Odd signs
        IF degreesInSign < 15:
            horaLord = "Sun"
            horaNumber = 1
        ELSE:
            horaLord = "Moon"
            horaNumber = 2
    ELSE:  // Even signs
        IF degreesInSign < 15:
            horaLord = "Moon"
            horaNumber = 1
        ELSE:
            horaLord = "Sun"
            horaNumber = 2
    END IF
    
    RETURN {
        lord: horaLord,
        number: horaNumber
    }
END FUNCTION
```

### 10.3 Calculate Drekkana (D-3)
```
FUNCTION calculateDrekkana(planetLongitude, signNumber):
    
    degreesInSign = planetLongitude mod 30
    
    // Each drekkana is 10 degrees
    drekkanaSize = 10
    drekkanaNumber = floor(degreesInSign / drekkanaSize) + 1
    
    // Determine starting sign
    IF signNumber IN [1, 3, 5, 7, 9, 11]:  // Odd signs
        startSign = signNumber
    ELSE:  // Even signs
        startSign = ((signNumber + 8) mod 12)
        IF startSign == 0:
            startSign = 12
    END IF
    
    // Calculate drekkana sign
    drekkanaSign = ((startSign + drekkanaNumber - 2) mod 12) + 1
    
    RETURN {
        sign: drekkanaSign,
        number: drekkanaNumber
    }
END FUNCTION
```

### 10.4 Calculate Saptamamsa (D-7)
```
FUNCTION calculateSaptamamsa(planetLongitude, signNumber):
    
    degreesInSign = planetLongitude mod 30
    
    // Each saptamamsa is 30/7 degrees
    saptamamsaSize = 30 / 7
    saptamamsaNumber = floor(degreesInSign / saptamamsaSize) + 1
    
    // For odd signs: count forward from sign
    // For even signs: count backward from 7th
    IF signNumber IN [1, 3, 5, 7, 9, 11]:  // Odd
        startSign = signNumber
        saptamamsaSign = ((startSign + saptamamsaNumber - 2) mod 12) + 1
    ELSE:  // Even
        startSign = ((signNumber + 6) mod 12)
        IF startSign == 0:
            startSign = 12
        saptamamsaSign = ((startSign - saptamamsaNumber + 13) mod 12)
        IF saptamamsaSign == 0:
            saptamamsaSign = 12
    END IF
    
    RETURN {
        sign: saptamamsaSign,
        number: saptamamsaNumber
    }
END FUNCTION
```

### 10.5 Calculate Dasamamsa (D-10)
```
FUNCTION calculateDasamamsa(planetLongitude, signNumber):
    
    degreesInSign = planetLongitude mod 30
    
    // Each dasamamsa is 3 degrees
    dasamamsaSize = 3
    dasamamsaNumber = floor(degreesInSign / dasamamsaSize) + 1
    
    // Odd signs: count from sign
    // Even signs: count from 9th
    IF signNumber IN [1, 3, 5, 7, 9, 11]:  // Odd
        startSign = signNumber
    ELSE:  // Even
        startSign = ((signNumber + 8) mod 12)
        IF startSign == 0:
            startSign = 12
    END IF
    
    dasamamsaSign = ((startSign + dasamamsaNumber - 2) mod 12) + 1
    
    RETURN {
        sign: dasamamsaSign,
        number: dasamamsaNumber
    }
END FUNCTION
```

### 10.6 Calculate Dwadasamsa (D-12)
```
FUNCTION calculateDwadasamsa(planetLongitude, signNumber):
    
    degreesInSign = planetLongitude mod 30
    
    // Each dwadasamsa is 2.5 degrees
    dwadasamsaSize = 2.5
    dwadasamsaNumber = floor(degreesInSign / dwadasamsaSize) + 1
    
    // Always count from the sign itself
    dwadasamsaSign = ((signNumber + dwadasamsaNumber - 2) mod 12) + 1
    
    RETURN {
        sign: dwadasamsaSign,
        number: dwadasamsaNumber
    }
END FUNCTION
```

### 10.7 Calculate Trimsamsa (D-30)
```
FUNCTION calculateTrimsamsa(planetLongitude, signNumber):
    
    degreesInSign = planetLongitude mod 30
    
    IF signNumber IN [1, 3, 5, 7, 9, 11]:  // Odd signs
        IF degreesInSign < 5:
            lord = "Mars"
        ELSE IF degreesInSign < 10:
            lord = "Saturn"
        ELSE IF degreesInSign < 18:
            lord = "Jupiter"
        ELSE IF degreesInSign < 25:
            lord = "Mercury"
        ELSE:
            lord = "Venus"
    ELSE:  // Even signs
        IF degreesInSign < 5:
            lord = "Venus"
        ELSE IF degreesInSign < 12:
            lord = "Mercury"
        ELSE IF degreesInSign < 20:
            lord = "Jupiter"
        ELSE IF degreesInSign < 25:
            lord = "Saturn"
        ELSE:
            lord = "Mars"
    END IF
    
    RETURN {
        lord: lord,
        degreesInSign: degreesInSign
    }
END FUNCTION
```

---

## 11. Dasha Calculations

### 11.1 Calculate Vimshottari Dasha Balance
```
FUNCTION calculateDashaBalance(moonLongitude, julianDay):
    
    // Find nakshatra and position within it
    nakshatra = findNakshatra(moonLongitude)
    
    // Get nakshatra lord and years
    nakshatraLords = {
        1: "Ketu", 2: "Venus", 3: "Sun", 4: "Moon", 5: "Mars",
        6: "Rahu", 7: "Jupiter", 8: "Saturn", 9: "Mercury",
        10: "Ketu", 11: "Venus", 12: "Sun", 13: "Moon", 14: "Mars",
        15: "Rahu", 16: "Jupiter", 17: "Saturn", 18: "Mercury",
        19: "Ketu", 20: "Venus", 21: "Sun", 22: "Moon", 23: "Mars",
        24: "Rahu", 25: "Jupiter", 26: "Saturn", 27: "Mercury"
    }
    
    dashaYears = {
        "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
        "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17
    }
    
    mahadashaLord = nakshatraLords[nakshatra.number]
    totalYears = dashaYears[mahadashaLord]
    
    // Calculate remaining portion
    // Each nakshatra is 13°20' = 800 minutes of arc
    nakshatraSpan = 13 + 20/60  // 13.333 degrees
    degreesInNakshatra = nakshatra.degreesInNakshatra
    
    // Portion elapsed
    elapsedPortion = degreesInNakshatra / nakshatraSpan
    
    // Portion remaining
    remainingPortion = 1 - elapsedPortion
    
    // Balance of dasha in years
    balanceYears = remainingPortion * totalYears
    
    RETURN {
        mahadashaLord: mahadashaLord,
        balanceYears: balanceYears,
        startDate: julianDay,
        endDate: julianDay + (balanceYears * 365.25)
    }
END FUNCTION
```

### 11.2 Calculate Full Dasha Sequence
```
FUNCTION calculateFullDashaSequence(dashaBalance, birthJulianDay):
    
    dashaSequence = [
        "Ketu", "Venus", "Sun", "Moon", "Mars",
        "Rahu", "Jupiter", "Saturn", "Mercury"
    ]
    
    dashaYears = {
        "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
        "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17
    }
    
    result = []
    currentDate = birthJulianDay
    
    // Find starting position
    startIndex = dashaSequence.indexOf(dashaBalance.mahadashaLord)
    
    // Add first dasha (balance)
    result.push({
        planet: dashaBalance.mahadashaLord,
        startDate: birthJulianDay,
        endDate: birthJulianDay + (dashaBalance.balanceYears * 365.25),
        years: dashaBalance.balanceYears
    })
    
    currentDate = result[0].endDate
    
    // Add remaining dashas in cycle
    FOR i FROM 1 TO 8:
        index = (startIndex + i) mod 9
        planet = dashaSequence[index]
        years = dashaYears[planet]
        
        result.push({
            planet: planet,
            startDate: currentDate,
            endDate: currentDate + (years * 365.25),
            years: years
        })
        
        currentDate = currentDate + (years * 365.25)
    END FOR
    
    RETURN result
END FUNCTION
```

### 11.3 Calculate Antardasha (Bhukti)
```
FUNCTION calculateAntardasha(mahadashaLord, startDate, years):
    
    dashaSequence = [
        "Ketu", "Venus", "Sun", "Moon", "Mars",
        "Rahu", "Jupiter", "Saturn", "Mercury"
    ]
    
    dashaYears = {
        "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
        "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17
    }
    
    result = []
    
    // Find starting position
    startIndex = dashaSequence.indexOf(mahadashaLord)
    
    // Total mahadasha years
    mahadashaTotal = dashaYears[mahadashaLord]
    
    currentDate = startDate
    
    FOR i FROM 0 TO 8:
        index = (startIndex + i) mod 9
        antardashaLord = dashaSequence[index]
        antardashaYears = dashaYears[antardashaLord]
        
        // Antardasha duration formula
        duration = (mahadashaTotal * antardashaYears) / 120
        durationDays = duration * 365.25
        
        result.push({
            antardashaLord: antardashaLord,
            mahadashaLord: mahadashaLord,
            startDate: currentDate,
            endDate: currentDate + durationDays,
            years: duration
        })
        
        currentDate = currentDate + durationDays
    END FOR
    
    RETURN result
END FUNCTION
```

---

## 12. Yoga Detection

### 12.1 Detect Raj Yoga
```
FUNCTION detectRajYoga(planetPositions, houses, ascendant):
    
    rajYogas = []
    
    // Get house lords
    kendraLords = []
    trikonaLords = []
    
    FOR house IN [1, 4, 7, 10]:  // Kendra
        lord = getHouseLord(house, ascendant)
        kendraLords.push(lord)
    END FOR
    
    FOR house IN [1, 5, 9]:  // Trikona
        lord = getHouseLord(house, ascendant)
        trikonaLords.push(lord)
    END FOR
    
    // Check for Kendra-Trikona connections
    FOR kLord IN kendraLords:
        FOR tLord IN trikonaLords:
            IF kLord == tLord:
                // Same planet ruling both kendra and trikona
                rajYogas.push({
                    type: "Kendra-Trikona Raja Yoga",
                    planet: kLord,
                    description: kLord + " rules both kendra and trikona"
                })
            ELSE IF areInConjunction(kLord, tLord, planetPositions):
                rajYogas.push({
                    type: "Conjunction Raja Yoga",
                    planets: [kLord, tLord]
                })
            ELSE IF areInMutualAspect(kLord, tLord, planetPositions):
                rajYogas.push({
                    type: "Mutual Aspect Raja Yoga",
                    planets: [kLord, tLord]
                })
            ELSE IF areInMutualExchange(kLord, tLord, planetPositions, houses):
                rajYogas.push({
                    type: "Parivartana Raja Yoga",
                    planets: [kLord, tLord]
                })
            END IF
        END FOR
    END FOR
    
    RETURN rajYogas
END FUNCTION
```

### 12.2 Detect Gaja Kesari Yoga
```
FUNCTION detectGajaKesariYoga(moonPosition, jupiterPosition, houses):
    
    // Check if Jupiter and Moon are in kendra from each other
    moonSign = floor(moonPosition / 30) + 1
    jupiterSign = floor(jupiterPosition / 30) + 1
    
    difference = abs(moonSign - jupiterSign)
    IF difference == 0:
        difference = 12
    END IF
    
    // Kendra positions: 1 (same), 4, 7, 10 signs apart
    IF difference IN [1, 4, 7, 10]:
        // Check if both are strong
        IF isPlanetStrong(moonPosition) AND isPlanetStrong(jupiterPosition):
            RETURN {
                present: true,
                strength: "Strong"
            }
        ELSE:
            RETURN {
                present: true,
                strength: "Weak"
            }
        END IF
    END IF
    
    RETURN { present: false }
END FUNCTION
```

### 12.3 Detect Dhana Yoga
```
FUNCTION detectDhanaYoga(planetPositions, houses, ascendant):
    
    dhanaYogas = []
    
    secondLord = getHouseLord(2, ascendant)
    eleventhLord = getHouseLord(11, ascendant)
    
    // Check 2nd and 11th lord association
    IF areInConjunction(secondLord, eleventhLord, planetPositions):
        dhanaYogas.push({
            type: "2-11 Dhana Yoga",
            planets: [secondLord, eleventhLord]
        })
    END IF
    
    // Check benefics in 2nd or 11th
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    
    FOR planet IN benefics:
        sign = floor(planetPositions[planet] / 30) + 1
        secondSign = ((ascendant + 1) mod 12)
        eleventhSign = ((ascendant + 10) mod 12)
        
        IF sign == secondSign OR sign == eleventhSign:
            dhanaYogas.push({
                type: "Benefic in Wealth House",
                planet: planet,
                house: (sign == secondSign) ? 2 : 11
            })
        END IF
    END FOR
    
    RETURN dhanaYogas
END FUNCTION
```

---

## 13. Dosha Detection

### 13.1 Detect Mangal Dosha
```
FUNCTION detectMangalDosha(marsPosition, ascendant, houses):
    
    marsSign = floor(marsPosition / 30) + 1
    ascSign = ascendant
    
    // Houses from lagna where Mars causes Manglik dosha
    manglikHouses = [1, 2, 4, 7, 8, 12]
    
    FOR house IN manglikHouses:
        houseSign = ((ascSign + house - 2) mod 12) + 1
        IF marsSign == houseSign:
            // Check exceptions
            IF isExceptionToMangalDosha(marsPosition, house):
                RETURN {
                    present: true,
                    cancelled: true,
                    house: house
                }
            ELSE:
                RETURN {
                    present: true,
                    cancelled: false,
                    house: house
                }
            END IF
        END IF
    END FOR
    
    RETURN { present: false }
END FUNCTION

FUNCTION isExceptionToMangalDosha(marsPosition, house):
    
    marsSign = floor(marsPosition / 30) + 1
    degreesInSign = marsPosition mod 30
    
    // Mars in its own sign
    IF marsSign IN [1, 8]:  // Aries or Scorpio
        RETURN true
    END IF
    
    // Mars in exaltation
    IF marsSign == 10 AND degreesInSign >= 28:  // Capricorn 28°
        RETURN true
    END IF
    
    // Mars conjunct with Jupiter or Moon
    // (Need full chart for this check)
    
    RETURN false
END FUNCTION
```

### 13.2 Detect Kaal Sarp Dosha
```
FUNCTION detectKaalSarpDosha(planetPositions, rahuPosition, ketuPosition):
    
    rahuSign = floor(rahuPosition / 30) + 1
    ketuSign = floor(ketuPosition / 30) + 1
    
    // All planets should be on one side of Rahu-Ketu axis
    allOnOneSide = true
    
    // Determine if axis is direct or reversed
    IF rahuSign < ketuSign:
        // Normal: Rahu before Ketu
        FOR each planet IN planetPositions (excluding Rahu, Ketu):
            planetSign = floor(planet / 30) + 1
            IF planetSign > rahuSign AND planetSign < ketuSign:
                // Planet between Rahu and Ketu
                allOnOneSide = false
                BREAK
            END IF
        END FOR
    ELSE:
        // Wraps around 0/360
        FOR each planet IN planetPositions (excluding Rahu, Ketu):
            planetSign = floor(planet / 30) + 1
            IF planetSign > rahuSign OR planetSign < ketuSign:
                // Planet between Rahu and Ketu (wraparound)
                allOnOneSide = false
                BREAK
            END IF
        END FOR
    END IF
    
    IF allOnOneSide:
        // Determine type
        IF rahuSign IN [6, 7, 8]:
            type = "Anant Kaal Sarp"
        ELSE IF rahuSign IN [9, 10, 11]:
            type = "Kulik Kaal Sarp"
        // ... more types
        
        RETURN {
            present: true,
            type: type,
            rahuSign: rahuSign,
            ketuSign: ketuSign
        }
    END IF
    
    RETURN { present: false }
END FUNCTION
```

### 13.3 Check Sade Sati
```
FUNCTION checkSadeSati(saturnTransitSign, moonNatalSign):
    
    // Sade Sati: Saturn transiting 12th, 1st, or 2nd from Moon
    twelfthFromMoon = ((moonNatalSign + 10) mod 12) + 1
    firstFromMoon = moonNatalSign
    secondFromMoon = ((moonNatalSign) mod 12) + 1
    
    IF saturnTransitSign == twelfthFromMoon:
        RETURN {
            active: true,
            phase: "Rising",
            houseFromMoon: 12
        }
    ELSE IF saturnTransitSign == firstFromMoon:
        RETURN {
            active: true,
            phase: "Peak",
            houseFromMoon: 1
        }
    ELSE IF saturnTransitSign == secondFromMoon:
        RETURN {
            active: true,
            phase: "Setting",
            houseFromMoon: 2
        }
    END IF
    
    RETURN { active: false }
END FUNCTION
```

---

## 14. Panchang Generation

### 14.1 Generate Daily Panchang
```
FUNCTION generatePanchang(date, latitude, longitude):
    
    // Calculate julian day for the date
    jd = calculateJDN(date.year, date.month, date.day, 6, 0, 0)
    
    // Get planetary positions
    sunLong = calculateSunLongitude(jd)
    moonLong = calculateMoonLongitude(jd)
    
    // Apply ayanamsa
    ayanamsa = calculateLahiriAyanamsa(jd)
    sunSidereal = tropicalToSidereal(sunLong, ayanamsa)
    moonSidereal = tropicalToSidereal(moonLong, ayanamsa)
    
    // Calculate Panchang elements
    tithi = calculateTithi(sunSidereal, moonSidereal)
    nakshatra = findNakshatra(moonSidereal)
    yoga = calculateYoga(sunSidereal, moonSidereal)
    karana = calculateKarana(tithi.number, tithi.fraction)
    
    // Day of week
    dayOfWeek = getDayOfWeek(date)
    
    // Sunrise and sunset
    sunTimes = calculateSunriseSunset(date, latitude, longitude)
    
    // Auspicious/inauspicious times
    rahuKaal = calculateRahuKaal(dayOfWeek, sunTimes.sunrise, sunTimes.sunset)
    yamaganda = calculateYamaganda(dayOfWeek, sunTimes.sunrise, sunTimes.sunset)
    gulika = calculateGulika(dayOfWeek, sunTimes.sunrise, sunTimes.sunset)
    
    RETURN {
        date: date,
        day: dayOfWeek,
        tithi: tithi,
        nakshatra: nakshatra,
        yoga: yoga,
        karana: karana,
        sunrise: sunTimes.sunrise,
        sunset: sunTimes.sunset,
        rahuKaal: rahuKaal,
        yamaganda: yamaganda,
        gulika: gulika,
        isVrata: checkVrata(date, tithi, nakshatra)
    }
END FUNCTION
```

### 14.2 Calculate Rahu Kaal
```
FUNCTION calculateRahuKaal(dayOfWeek, sunrise, sunset):
    
    // Duration of day
    dayDuration = sunset - sunrise
    
    // Each part is 1/8 of day duration
    partDuration = dayDuration / 8
    
    // Rahu Kaal sequence based on day
    rahuSequence = {
        "Sunday": 8,      // 8th part
        "Monday": 2,      // 2nd part
        "Tuesday": 7,     // 7th part
        "Wednesday": 5,   // 5th part
        "Thursday": 6,    // 6th part
        "Friday": 4,      // 4th part
        "Saturday": 3     // 3rd part
    }
    
    rahuPart = rahuSequence[dayOfWeek]
    
    startTime = sunrise + (rahuPart - 1) * partDuration
    endTime = sunrise + rahuPart * partDuration
    
    RETURN {
        start: startTime,
        end: endTime,
        duration: partDuration
    }
END FUNCTION
```

---

## 15. Compatibility Matching

### 15.1 Ashta Koota Matching
```
FUNCTION calculateAshtaKoota(boyChart, girlChart):
    
    totalPoints = 0
    results = {}
    
    // 1. Varna Koota (1 point)
    varnaPoints = calculateVarnaKoota(boyChart.moonSign, girlChart.moonSign)
    results.varna = varnaPoints
    totalPoints += varnaPoints
    
    // 2. Vashya Koota (2 points)
    vashyaPoints = calculateVashyaKoota(boyChart.moonSign, girlChart.moonSign)
    results.vashya = vashyaPoints
    totalPoints += vashyaPoints
    
    // 3. Tara Koota (3 points)
    taraPoints = calculateTaraKoota(boyChart.nakshatra, girlChart.nakshatra)
    results.tara = taraPoints
    totalPoints += taraPoints
    
    // 4. Yoni Koota (4 points)
    yoniPoints = calculateYoniKoota(boyChart.nakshatra, girlChart.nakshatra)
    results.yoni = yoniPoints
    totalPoints += yoniPoints
    
    // 5. Graha Maitri (5 points)
    grahaMaitriPoints = calculateGrahaMaitri(boyChart.moonSign, girlChart.moonSign)
    results.grahaMaitri = grahaMaitriPoints
    totalPoints += grahaMaitriPoints
    
    // 6. Gana Koota (6 points)
    ganaPoints = calculateGanaKoota(boyChart.nakshatra, girlChart.nakshatra)
    results.gana = ganaPoints
    totalPoints += ganaPoints
    
    // 7. Bhakoot Koota (7 points)
    bhakootPoints = calculateBhakootKoota(boyChart.moonSign, girlChart.moonSign)
    results.bhakoot = bhakootPoints
    totalPoints += bhakootPoints
    
    // 8. Nadi Koota (8 points)
    nadiPoints = calculateNadiKoota(boyChart.nakshatra, girlChart.nakshatra)
    results.nadi = nadiPoints
    totalPoints += nadiPoints
    
    RETURN {
        totalPoints: totalPoints,
        maxPoints: 36,
        percentage: (totalPoints / 36) * 100,
        details: results,
        recommendation: getCompatibilityRecommendation(totalPoints)
    }
END FUNCTION
```

### 15.2 Gana Matching
```
FUNCTION calculateGanaKoota(boyNakshatra, girlNakshatra):
    
    devaGana = [1, 5, 7, 8, 13, 15, 17, 22, 27]  // Ashwini, Mrigashira, etc.
    manushyaGana = [2, 4, 6, 11, 20, 25]  // Bharani, Rohini, etc.
    rakshasaGana = [3, 9, 10, 14, 16, 18, 19, 21, 23, 24, 26]  // Others
    
    boyGana = getGana(boyNakshatra)
    girlGana = getGana(girlNakshatra)
    
    // Matching rules
    IF boyGana == girlGana:
        RETURN 6  // Same gana
    ELSE IF (boyGana == "Deva" AND girlGana == "Manushya") OR
            (boyGana == "Manushya" AND girlGana == "Deva"):
        RETURN 6  // Compatible
    ELSE IF (boyGana == "Manushya" AND girlGana == "Manushya"):
        RETURN 6
    ELSE IF (boyGana == "Rakshasa" AND girlGana == "Rakshasa"):
        RETURN 6
    ELSE:
        RETURN 0  // Incompatible
    END IF
END FUNCTION
```

### 15.3 Nadi Matching
```
FUNCTION calculateNadiKoota(boyNakshatra, girlNakshatra):
    
    adiNadi = [1, 6, 7, 12, 13, 18, 19, 24, 25]
    madhyaNadi = [2, 5, 8, 11, 14, 17, 20, 23, 26]
    antyaNadi = [3, 4, 9, 10, 15, 16, 21, 22, 27]
    
    boyNadi = getNadi(boyNakshatra)
    girlNadi = getNadi(girlNakshatra)
    
    // Same nadi is inauspicious (zero points)
    IF boyNadi == girlNadi:
        RETURN 0
    ELSE:
        RETURN 8
    END IF
END FUNCTION
```

---

## Helper Functions

```
FUNCTION toRadians(degrees):
    RETURN degrees * (PI / 180)
END FUNCTION

FUNCTION toDegrees(radians):
    RETURN radians * (180 / PI)
END FUNCTION

FUNCTION floor(value):
    RETURN largest integer <= value
END FUNCTION

FUNCTION mod(value, divisor):
    RETURN remainder of value/divisor
END FUNCTION

FUNCTION isExalted(planet, sign):
    exaltationSigns = {
        "Sun": 1,       // Aries
        "Moon": 2,      // Taurus
        "Mars": 10,     // Capricorn
        "Mercury": 6,   // Virgo
        "Jupiter": 4,   // Cancer
        "Venus": 12,    // Pisces
        "Saturn": 7     // Libra
    }
    RETURN exaltationSigns[planet] == sign
END FUNCTION

FUNCTION isDebilitated(planet, sign):
    debilitationSigns = {
        "Sun": 7,       // Libra
        "Moon": 8,      // Scorpio
        "Mars": 4,      // Cancer
        "Mercury": 12,  // Pisces
        "Jupiter": 10,  // Capricorn
        "Venus": 6,     // Virgo
        "Saturn": 1     // Aries
    }
    RETURN debilitationSigns[planet] == sign
END FUNCTION
```

---

*Algorithm Version: 1.0*
*Last Updated: March 2026*
