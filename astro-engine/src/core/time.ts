/**
 * Time conversion utilities
 */

/**
 * Calculate Julian Day Number
 * @param year Year (e.g., 2024)
 * @param month Month (1-12)
 * @param day Day (1-31)
 * @param hour Hour (0-23)
 * @param minute Minute (0-59)
 * @param second Second (0-59)
 * @returns Julian Day Number
 */
export function calculateJDN(
  year: number,
  month: number,
  day: number,
  hour: number = 0,
  minute: number = 0,
  second: number = 0
): number {
  // Adjust month and year for January and February
  let a = year;
  let m = month;
  if (m <= 2) {
    a -= 1;
    m += 12;
  }

  // Calculate Julian Day at noon UT
  const A = Math.floor(a / 100);
  const B = 2 - A + Math.floor(A / 4);

  let JD = Math.floor(365.25 * (a + 4716)) +
           Math.floor(30.6001 * (m + 1)) +
           day + B - 1524.5;

  // Add time fraction
  const timeFraction = (hour + minute / 60 + second / 3600) / 24;
  JD += timeFraction;

  return JD;
}

/**
 * Convert standard time to Local Mean Time
 * @param standardTime Standard time (hours)
 * @param birthLongitude Birth place longitude
 * @param standardMeridian Standard meridian for timezone
 * @returns Local Mean Time in hours
 */
export function convertToLMT(
  standardTime: number,
  birthLongitude: number,
  standardMeridian: number
): number {
  // Each degree of longitude = 4 minutes time difference
  const longitudeDifference = birthLongitude - standardMeridian;
  const timeDifferenceHours = longitudeDifference * 4 / 60;
  
  return standardTime + timeDifferenceHours;
}

/**
 * Calculate sidereal time at Greenwich
 * @param julianDay Julian Day Number
 * @returns Sidereal time in degrees
 */
export function calculateGMST(julianDay: number): number {
  // Julian centuries from J2000.0
  const T = (julianDay - 2451545.0) / 36525.0;
  
  // Greenwich Mean Sidereal Time
  let gmst = 280.46061837 + 360.98564736629 * (julianDay - 2451545.0);
  gmst += 0.000387933 * T * T;
  gmst -= (T * T * T) / 38710000.0;
  
  // Normalize to 0-360
  gmst = gmst % 360;
  if (gmst < 0) gmst += 360;
  
  return gmst;
}

/**
 * Calculate local sidereal time
 * @param julianDay Julian Day Number
 * @param longitude Longitude in degrees (East positive)
 * @returns Local sidereal time in degrees
 */
export function calculateLST(julianDay: number, longitude: number): number {
  const gmst = calculateGMST(julianDay);
  let lst = gmst + longitude;
  
  // Normalize to 0-360
  lst = lst % 360;
  if (lst < 0) lst += 360;
  
  return lst;
}

/**
 * Convert degrees to hours
 * @param degrees Angle in degrees
 * @returns Angle in hours (15 degrees = 1 hour)
 */
export function degreesToHours(degrees: number): number {
  return degrees / 15.0;
}

/**
 * Convert hours to degrees
 * @param hours Time in hours
 * @returns Angle in degrees
 */
export function hoursToDegrees(hours: number): number {
  return hours * 15.0;
}
