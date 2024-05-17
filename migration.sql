CREATE TABLE
	CONTRIBUTORS (
		id UUID PRIMARY KEY,
		nama VARCHAR(50) NOT NULL,
		jenis_kelamin INT NOT NULL CHECK (jenis_kelamin IN (0, 1)),
		kewarganegaraan VARCHAR(50) NOT NULL
	)
;

CREATE TABLE
	SUTRADARA (
		id UUID PRIMARY KEY,
		FOREIGN KEY (id) REFERENCES CONTRIBUTORS (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	TAYANGAN (
		id UUID PRIMARY KEY,
		judul VARCHAR(100) NOT NULL,
		sinopsis VARCHAR(255) NOT NULL,
		asal_negara VARCHAR(50) NOT NULL,
		sinopsis_trailer VARCHAR(255) NOT NULL,
		url_video_trailer VARCHAR(255) NOT NULL,
		release_date_trailer DATE NOT NULL,
		id_sutradara UUID,
		FOREIGN KEY (id_sutradara) REFERENCES SUTRADARA (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	PENGGUNA (
		username VARCHAR(50) PRIMARY KEY,
		PASSWORD VARCHAR(50) NOT NULL,
		id_tayangan UUID,
		negara_asal VARCHAR(50) NOT NULL,
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	PAKET (
		nama VARCHAR(50) PRIMARY KEY,
		harga INT CHECK (harga >= 0) NOT NULL,
		resolusi_layar VARCHAR(50) NOT NULL
	)
;

CREATE TABLE
	DUKUNGAN_PERANGKAT (
		nama_paket VARCHAR(50),
		dukungan_perangkat VARCHAR(50),
		PRIMARY KEY (nama_paket, dukungan_perangkat),
		FOREIGN KEY (nama_paket) REFERENCES PAKET (nama)
	)
;

CREATE TABLE
	TRANSACTION (
		username VARCHAR(50),
		start_date_time DATE,
		end_date_time DATE,
		nama_paket VARCHAR(50),
		metode_pembayaran VARCHAR(50) NOT NULL,
		timestamp_pembayaran DATE NOT NULL,
		PRIMARY KEY (username, start_date_time),
		FOREIGN KEY (username) REFERENCES PENGGUNA (username) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	PENULIS_SKENARIO (
		id UUID PRIMARY KEY,
		FOREIGN KEY (id) REFERENCES CONTRIBUTORS (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	PEMAIN (
		id UUID PRIMARY KEY,
		FOREIGN KEY (id) REFERENCES CONTRIBUTORS (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	MEMAINKAN_TAYANGAN (
		id_tayangan UUID,
		id_pemain UUID,
		PRIMARY KEY (id_tayangan, id_pemain),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id) ON UPDATE CASCADE ON DELETE RESTRICT,
		FOREIGN KEY (id_pemain) REFERENCES CONTRIBUTORS (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	MENULIS_SKENARIO_TAYANGAN (
		id_tayangan UUID,
		id_pemain UUID,
		PRIMARY KEY (id_tayangan, id_pemain),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id) ON UPDATE CASCADE ON DELETE RESTRICT,
		FOREIGN KEY (id_pemain) REFERENCES CONTRIBUTORS (id) ON UPDATE CASCADE ON DELETE RESTRICT
	)
;

CREATE TABLE
	GENRE_TAYANGAN (
		id_tayangan UUID PRIMARY KEY,
		genre VARCHAR(50) NOT NULL
	)
;

CREATE TABLE
	PERUSAHAAN_PRODUKSI (nama VARCHAR(100) PRIMARY KEY)
;

CREATE TABLE
	PERSETUJUAN (
		nama VARCHAR(100),
		id_tayangan UUID,
		tanggal_persetujuan DATE,
		durasi INT NOT NULL CHECK (durasi >= 0),
		biaya INT NOT NULL CHECK (biaya >= 0),
		tanggal_mulai_penayangan DATE NOT NULL,
		PRIMARY KEY (nama, id_tayangan, tanggal_persetujuan),
		FOREIGN KEY (nama) REFERENCES PERUSAHAAN_PRODUKSI (nama),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id)
	)
;

CREATE TABLE
	SERIES (
		id_tayangan UUID PRIMARY KEY,
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id)
	)
;

CREATE TABLE
	FILM (
		id_tayangan UUID PRIMARY KEY,
		url_video_film VARCHAR(255) NOT NULL,
		release_date_film DATE NOT NULL,
		durasi_film INT NOT NULL DEFAULT 0,
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id)
	)
;

CREATE TABLE
	EPISODE (
		id_series UUID,
		sub_judul VARCHAR(100),
		sinopsis VARCHAR(255) NOT NULL,
		durasi INT NOT NULL DEFAULT 0,
		url_video VARCHAR(255) NOT NULL,
		release_date DATE NOT NULL,
		PRIMARY KEY (id_series, sub_judul),
		FOREIGN KEY (id_series) REFERENCES SERIES (id_tayangan)
	)
;

CREATE TABLE
	ULASAN (
		id_tayangan UUID,
		username VARCHAR(50),
		TIMESTAMP TIMESTAMP PRIMARY KEY,
		rating INT NOT NULL DEFAULT 0,
		deskripsi VARCHAR(255),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id),
		FOREIGN KEY (username) REFERENCES PENGGUNA (username)
	)
;

CREATE TABLE
	DAFTAR_FAVORIT (
		TIMESTAMP TIMESTAMP,
		username VARCHAR(50),
		judul VARCHAR(50) NOT NULL,
		PRIMARY KEY (TIMESTAMP, username),
		FOREIGN KEY (username) REFERENCES PENGGUNA (username)
	)
;

CREATE TABLE
	TAYANGAN_MEMILIKI_DAFTAR_FAVORIT (
		id_tayangan UUID,
		TIMESTAMP TIMESTAMP,
		username VARCHAR(50),
		PRIMARY KEY (id_tayangan, TIMESTAMP, username),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id),
		FOREIGN KEY (TIMESTAMP, username) REFERENCES DAFTAR_FAVORIT (TIMESTAMP, username)
	)
;

CREATE TABLE
	RIWAYAT_NONTON (
		id_tayangan UUID,
		username VARCHAR(50),
		start_date_time TIMESTAMP,
		end_date_time TIMESTAMP NOT NULL,
		PRIMARY KEY (username, start_date_time),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id),
		FOREIGN KEY (username) REFERENCES PENGGUNA (username)
	)
;

CREATE TABLE
	TAYANGAN_TERUNDUH (
		id_tayangan UUID,
		username VARCHAR(50),
		TIMESTAMP TIMESTAMP,
		PRIMARY KEY (id_tayangan, username, TIMESTAMP),
		FOREIGN KEY (id_tayangan) REFERENCES TAYANGAN (id),
		FOREIGN KEY (username) REFERENCES PENGGUNA (username)
	)
;