# Kraken

## API

### URLs clés de l'API REST Kraken (Spot)

Base de l'API : `https://api.kraken.com`

#### Informations système & référence (sans paramètre obligatoire)

| Type       | URL Complète                                   | Description                                          |
| :--------- | :--------------------------------------------- | :--------------------------------------------------- |
| **Public** | `https://api.kraken.com/0/public/Time`         | Heure du serveur (utile pour tester la connectivité) |
| **Public** | `https://api.kraken.com/0/public/SystemStatus` | Statut actuel du système de trading                  |
| **Public** | `https://api.kraken.com/0/public/Assets`       | Informations sur les actifs disponibles              |
| **Public** | `https://api.kraken.com/0/public/AssetPairs`   | Métadonnées des paires tradables                     |

---

#### Données de marché (Ticker, OHLC)

| Type       | URL Complète                                                     | Description                                               |
| :--------- | :--------------------------------------------------------------- | :-------------------------------------------------------- |
| **Public** | `https://api.kraken.com/0/public/Ticker`                         | Ticker<br>**Nécessite le paramètre `pair`**               |
| **Public** | `https://api.kraken.com/0/public/Ticker?pair=XBTUSD`             | **Ticker récent** pour XBT/USD                            |
| **Public** | `https://api.kraken.com/0/public/OHLC`                           | OHLC<br>**Nécessite les paramètres `pair` et `interval`** |
| **Public** | `https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=5`    | OHLC<br>**BTCUSD en 5m**                                  |
| **Public** | `https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=60`   | OHLC<br>**BTCUSD en 1h**                                  |
| **Public** | `https://api.kraken.com/0/public/OHLC?pair=ETHUSD&interval=1440` | OHLC<br>**ETHUSD en 1d**                                  |

---

#### Carnet d'ordres (Depth)

| Type       | URL Complète                                                  | Description                                                    |
| :--------- | :------------------------------------------------------------ | :------------------------------------------------------------- |
| **Public** | `https://api.kraken.com/0/public/Depth?pair=XBTUSD&count=100` | Carnet d'ordres pour le **Bitcoin (XBT/USD)**, **100 niveaux** |
| **Public** | `https://api.kraken.com/0/public/Depth?pair=ETHUSD&count=10`  | Carnet d'ordres pour l'**Ethereum (ETH/USD)**, **10 niveaux**  |
| **Public** | `https://api.kraken.com/0/public/Depth?pair=XBTUSD`           | Carnet d'ordres pour **XBT/USD**, nombre de niveaux par défaut |

---

#### Transactions & spread (Trades, Spread)

| Type       | URL Complète                                                   | Description                                                                |
| :--------- | :------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **Public** | `https://api.kraken.com/0/public/Trades`                       | Historique des transactions publiques<br>**Nécessite le paramètre `pair`** |
| **Public** | `https://api.kraken.com/0/public/Trades?pair=XBTUSD`           | **Transactions récentes** pour XBT/USD                                     |
| **Public** | `https://api.kraken.com/0/public/Trades?pair=ETHUSD&count=100` | **100 dernières transactions** pour ETH/USD                                |
| **Public** | `https://api.kraken.com/0/public/Spread`                       | Données de spread<br>**Nécessite le paramètre `pair`**                     |
| **Public** | `https://api.kraken.com/0/public/Spread?pair=XBTUSD`           | **Spread récent** pour XBT/USD                                             |
| **Public** | `https://api.kraken.com/0/public/Spread?pair=ETHUSD`           | **Spread récent** pour ETH/USD                                             |

---

#### Endpoints privés (Balance, Orders…)

| Type      | URL Complète                                          | Description                              |
| :-------- | :---------------------------------------------------- | :--------------------------------------- |
| **Privé** | `https://api.kraken.com/0/private/Balance`            | Soldes de tous les actifs du compte      |
| **Privé** | `https://api.kraken.com/0/private/TradeBalance`       | Solde de trading                         |
| **Privé** | `https://api.kraken.com/0/private/OpenOrders`         | Ordres actuellement ouverts              |
| **Privé** | `https://api.kraken.com/0/private/ClosedOrders`       | Ordres clôturés                          |
| **Privé** | `https://api.kraken.com/0/private/QueryOrders`        | Informations sur des ordres spécifiques  |
| **Privé** | `https://api.kraken.com/0/private/AddOrder`           | Passer un nouvel ordre                   |
| **Privé** | `https://api.kraken.com/0/private/CancelOrder`        | Annuler un ordre                         |
| **Privé** | `https://api.kraken.com/0/private/GetWebSocketsToken` | Obtenir un token pour le WebSocket privé |

---

### WebSocket (flux temps réel)

Kraken propose une API WebSocket (v2, recommandée) pour les flux en temps réel, distincte de l'API REST.

| Type       | URL de base                   | Description                                             |
| :--------- | :---------------------------- | :------------------------------------------------------ |
| **Public** | `wss://ws.kraken.com/v2`      | Flux publics : ticker, trades, book, OHLC, spread…      |
| **Privé**  | `wss://ws-auth.kraken.com/v2` | Flux privés : ordres, exécutions, soldes (auth requise) |
| Legacy     | `wss://ws.kraken.com`         | API WebSocket v1 (dépréciée, à éviter pour du neuf)     |

> **Note** : l'accès au WebSocket privé nécessite un token obtenu via l'endpoint REST `https://api.kraken.com/0/private/GetWebSocketsToken` (authentification HMAC-SHA512 requise).

### Commentaires

#### Note

> Les endpoints marqués **Privé** nécessitent une authentification via votre clé API et votre secret (signature HMAC-SHA512). Les endpoints **Public** sont accessibles sans authentification.

#### Rappel

> Les endpoints REST publics sont tous sous le préfixe `/0/public/`, et les endpoints privés sous `/0/private/`. Omettre ce préfixe renvoie une erreur.

#### Paramètres obligatoires

> Les endpoints `Ticker`, `OHLC`, `Depth`, `Trades` et `Spread` nécessitent au minimum le paramètre `pair`. Sans lui, l'URL seule renvoie une erreur.

#### Nomenclature des paires

> Kraken utilise souvent des noms historiques (`XBTUSD` pour Bitcoin, et non `BTCUSD`). En cas de doute, vérifier le nom exact via `AssetPairs`.

### Auth

* [ ] API privé
* [ ] WebSocket

#### 1. Authentification API privée (REST)

Tous les endpoints sous `/0/private/` exigent une signature **HMAC-SHA512** calculée à partir de votre clé secrète. La clé API (publique) identifie le compte ; la signature authentifie chaque appel et change à chaque requête.

**Étapes :**

1. **Générer une paire de clés API** dans votre compte Kraken : Settings → API → *Create API key*. Vous obtenez une **clé publique** (`API-Key`) et une **clé privée** secrète (`API-Sign` secret).
2. **Construire le corps de la requête** : pour un endpoint privé, les paramètres sont envoyés en `POST` avec un paramètre `nonce` (entier incrémental, typiquement le timestamp en millisecondes).
3. **Calculer la signature** exactement comme suit :

   * `post_data` = chaîne des paramètres encodés URL (`nonce=...&param1=...`)
   * `encoded` = `str(nonce) + post_data`
   * `message` = `URI_path` (ex: `/0/private/Balance`) + `SHA256(encoded)` (en bytes bruts)
   * **Décoder la clé secrète en base64** avant de l'utiliser comme clé HMAC
   * `signature` = `BASE64( HMAC-SHA512( key=secret_décodé, message=message ) )`

4. **Envoyer les en-têtes HTTP** avec chaque requête privée :

   * `API-Key: <votre_clé_publique>`
   * `API-Sign: <signature_calculée>`

> **Important** : la clé secrète doit être **décodée en base64** avant d'être utilisée comme clé HMAC. Utiliser la chaîne base64 brute est l'erreur la plus fréquente.

📖 Référence : <https://docs.kraken.com/api/docs/guides/rest-authentication>

---

#### 2. Authentification WebSocket privé

Le WebSocket privé (`wss://ws-auth.kraken.com/v2`) n'utilise pas de signature par message. Il repose sur un **token à courte durée de vie**, obtenu via un appel REST privé préalable.

**Étapes :**

1. **Obtenir un token** en appelant l'endpoint REST **`POST /0/private/GetWebSocketsToken`**, signé exactement comme n'importe quel endpoint privé REST (voir section 1). Documentation de l'endpoint : <https://docs.kraken.com/api/docs/rest-api/get-websockets-token>
2. **Récupérer le token** dans la réponse JSON (champ `token`). Ce token est valide **15 minutes**.
3. **Se connecter** à `wss://ws-auth.kraken.com/v2`.
4. **Inclure le token** dans chaque message de souscription aux canaux privés (`ownTrades`, `openOrders`, etc.).
5. **Rafraîchir le token** avant son expiration (ou avant toute reconnexion) en rappelant `GetWebSocketsToken`.

> **Prérequis** : la clé API doit avoir la permission **« Access WebSockets »** activée dans les paramètres Kraken, sinon `GetWebSocketsToken` échouera.

📖 Références :

* Guide général WebSocket : <https://docs.kraken.com/api/docs/guides/websockets>
* Authentification WebSocket : <https://docs.kraken.com/api/docs/guides/websockets-authentication>
