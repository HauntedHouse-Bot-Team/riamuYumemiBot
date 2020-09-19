USE bot;

CREATE TABLE `masturbation_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fap_material` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `guild` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=225 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `ghosts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `ghost_id` int(10) unsigned NOT NULL COMMENT '幽霊屋敷のユーザーID',
  `gold` bigint(20) unsigned NOT NULL DEFAULT '9000' COMMENT 'サーバー内通貨(みつは)',
  `del_flg` tinyint(1) NOT NULL DEFAULT '0' COMMENT '削除フラグ',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UNQ_GHOST_ID` (`ghost_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
