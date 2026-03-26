/**
 * Ayanamsa calculations
 * Lahiri Ayanamsa (Chitrapaksha) - Standard in Indian astrology
 */

/**
 * Calculate Lahiri Ayanamsa for a given Julian Day
 * @param julianDay Julian Day Number
 * @returns Ayanamsa in degrees
 */
export function calculateLahiriAyanamsa(julianDay: number): number {
  // Julian centuries from J2000.0
  const T = (julianDay - 2451545.0) / 36525.0;
  
  // Lahiri ayanamsa formula (simplified)
  // More precise formula can be implemented later
  const ayanamsa = 23.8565 + (T * 50.29 / 3600);
  
  return ayanamsa;
}

/**
 * Convert tropical longitude to sidereal
 * @param tropicalLongitude Longitude in tropical zodiac
 * @param ayanamsa Ayanamsa value
 * @returns Sidereal longitude
 */
export function tropicalToSidereal(
  tropicalLongitude: number,
  ayanamsa: number
): number {
  let sidereal = tropicalLongitude - ayanamsa;
  
  // Normalize to 0-360 range
  while (sidereal < 0) {
    sidereal += 360;
  }
  while (sidereal >= 360) {
    sidereal -= 360;
  }
  
  return sidereal;
}

/**
 * Convert sidereal longitude to tropical
 * @param siderealLongitude Longitude in sidereal zodiac
 * @param ayanamsa Ayanamsa value
 * @returns Tropical longitude
 */
export function siderealToTropical(
  siderealLongitude: number,
  ayanamsa: number
): number {
  let tropical = siderealLongitude + ayanamsa;
  
  // Normalize to 0-360 range
  while (tropical < 0) {
    tropical += 360;
  }
  while (tropical >= 360) {
    tropical -= 360;
  }
  
  return tropical;
}
