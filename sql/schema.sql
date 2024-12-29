SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `body_battery` (
  `id` int(10) UNSIGNED NOT NULL,
  `low_body_battery` smallint(5) DEFAULT NULL,
  `high_body_battery` smallint(5) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `calories` (
  `id` int(10) UNSIGNED NOT NULL,
  `resting_calories` int(6) DEFAULT NULL,
  `active_calories` int(6) DEFAULT NULL,
  `total_calories` int(6) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `heart_beat` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `bpm` int(11) UNSIGNED NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `heart_rate` (
  `id` int(10) UNSIGNED NOT NULL,
  `resting_hr` smallint(5) UNSIGNED DEFAULT NULL,
  `wellness_max_avg_hr` smallint(5) UNSIGNED DEFAULT NULL,
  `wellness_min_avg_hr` smallint(5) UNSIGNED DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `sleep` (
  `id` int(10) UNSIGNED NOT NULL,
  `light_time` int(6) DEFAULT NULL,
  `deep_time` int(6) DEFAULT NULL,
  `rem_time` int(6) DEFAULT NULL,
  `awake_time` int(6) DEFAULT NULL,
  `total_sleep_time` int(6) DEFAULT NULL,
  `sleep_start_time` time DEFAULT NULL,
  `sleep_end_time` time DEFAULT NULL,
  `sleep_start_seconds_to_midnight` int(6) DEFAULT NULL,
  `sleep_end_seconds_to_midnight` int(6) DEFAULT NULL,
  `body_battery_change` smallint(6) DEFAULT NULL,
  `respiration` smallint(6) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `steps` (
  `id` int(10) UNSIGNED NOT NULL,
  `total_steps` int(6) DEFAULT NULL,
  `total_distance` int(6) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `stress` (
  `id` int(10) UNSIGNED NOT NULL,
  `rest_stress_duration` int(6) DEFAULT NULL,
  `low_stress_duration` int(6) DEFAULT NULL,
  `medium_stress_duration` int(6) DEFAULT NULL,
  `high_stress_duration` int(11) DEFAULT NULL,
  `overall_stress_level` smallint(6) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


ALTER TABLE `body_battery`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `calories`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `heart_beat`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `heart_rate`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `sleep`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `steps`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `stress`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `body_battery`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `calories`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `heart_beat`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `heart_rate`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `sleep`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `steps`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

ALTER TABLE `stress`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;