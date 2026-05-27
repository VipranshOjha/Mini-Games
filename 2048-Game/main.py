import pygame
import random
import math
import os

pygame.init()

FPS = 60

HEADER_HEIGHT = 80
FOOTER_HEIGHT = 34
BOARD_SIZE    = 560          

WIDTH  = BOARD_SIZE
HEIGHT = BOARD_SIZE + HEADER_HEIGHT + FOOTER_HEIGHT

ROWS = 4
COLS = 4

RECT_HEIGHT = BOARD_SIZE // ROWS   
RECT_WIDTH  = BOARD_SIZE // COLS   

BOARD_Y = HEADER_HEIGHT            

OUTLINE_COLOR     = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR  = (205, 192, 180)
FONT_COLOR        = (119, 110, 101)
HEADER_BG         = (250, 248, 239)
SCORE_BG          = (187, 173, 160)
SCORE_LABEL_COLOR = (238, 228, 218)
SCORE_VALUE_COLOR = (255, 255, 255)

FONT        = pygame.font.SysFont("comicsans", 46, bold=True)
FONT_SMALL  = pygame.font.SysFont("comicsans", 15, bold=True)
FONT_MED    = pygame.font.SysFont("comicsans", 24, bold=True)
FONT_TITLE  = pygame.font.SysFont("comicsans", 44, bold=True)
FONT_POPUP  = pygame.font.SysFont("comicsans", 36, bold=True)
FONT_FOOTER = pygame.font.SysFont("comicsans", 13)

MOVE_VEL = 20

HIGHSCORE_FILE = "highscore.txt"

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95,  59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row   = row
        self.col   = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT + BOARD_Y

    def get_color(self):
        idx = min(int(math.log2(self.value)) - 1, len(self.COLORS) - 1)
        return self.COLORS[idx]

    def draw(self, window):
        pygame.draw.rect(window, self.get_color(),
                         (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        text = FONT.render(str(self.value), True, FONT_COLOR)
        window.blit(text, (
            self.x + RECT_WIDTH  // 2 - text.get_width()  // 2,
            self.y + RECT_HEIGHT // 2 - text.get_height() // 2,
        ))

    def set_pos(self, ceil=False):
        fn = math.ceil if ceil else math.floor
        self.row = fn((self.y - BOARD_Y) / RECT_HEIGHT)
        self.col = fn(self.x             / RECT_WIDTH)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]


class ScorePopup:
    def __init__(self, value, x, y):
        self.text     = f"+{value}"
        self.x        = float(x)
        self.y        = float(y)
        self.lifetime = 70
        self.age      = 0

    def update(self):
        self.age += 1
        self.y   -= 2.0

    def draw(self, window):
        p = self.age / self.lifetime
        if   p < 0.15: alpha = int(255 * (p / 0.15))
        elif p < 0.65: alpha = 255
        else:          alpha = int(255 * (1 - (p - 0.65) / 0.35))
        alpha = max(0, min(255, alpha))

        for dx, dy in ((-2,0),(2,0),(0,-2),(0,2)):
            s = FONT_POPUP.render(self.text, True, (255, 255, 255))
            s.set_alpha(alpha)
            window.blit(s, (self.x - s.get_width()//2 + dx,
                            self.y - s.get_height()//2 + dy))
        s = FONT_POPUP.render(self.text, True, (247, 95, 59))
        s.set_alpha(alpha)
        window.blit(s, (self.x - s.get_width()//2, self.y - s.get_height()//2))

    @property
    def alive(self): return self.age < self.lifetime


class Button:
    def __init__(self, x, y, w, h, label):
        self.rect    = pygame.Rect(x, y, w, h)
        self.label   = label
        self.hovered = False

    def draw(self, window):
        color = (143, 122, 102) if self.hovered else SCORE_BG
        pygame.draw.rect(window, color, self.rect, border_radius=6)
        text = FONT_SMALL.render(self.label, True, SCORE_VALUE_COLOR)
        window.blit(text, (
            self.rect.centerx - text.get_width()  // 2,
            self.rect.centery - text.get_height() // 2,
        ))

    def check_hover(self, pos): self.hovered = self.rect.collidepoint(pos)
    def is_clicked(self, pos):  return self.rect.collidepoint(pos)


def load_highscore():
    try:
        with open(HIGHSCORE_FILE) as f:
            return max(0, int(f.read().strip()))
    except Exception:
        return 0

def save_highscore(score):
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(score))
    except Exception:
        pass


def draw_score_card(window, label, value, x, y, w, h):
    pygame.draw.rect(window, SCORE_BG, (x, y, w, h), border_radius=6)
    lbl = FONT_SMALL.render(label, True, SCORE_LABEL_COLOR)
    val = FONT_MED.render(str(value),  True, SCORE_VALUE_COLOR)
    window.blit(lbl, (x + w//2 - lbl.get_width()//2, y + 5))
    window.blit(val, (x + w//2 - val.get_width()//2, y + h - val.get_height() - 5))


def draw_header(window, score, best_score, btn):

    window.fill(HEADER_BG, (0, 0, WIDTH, HEADER_HEIGHT))

    title = FONT_TITLE.render("2048", True, FONT_COLOR)
    window.blit(title, (14, HEADER_HEIGHT // 2 - title.get_height() // 2))

    MARGIN   = 10   
    CARD_W   = 80
    CARD_H   = 54
    BTN_W    = 86
    BTN_H    = 34

    card_y = HEADER_HEIGHT // 2 - CARD_H // 2
    btn_y  = HEADER_HEIGHT // 2 - BTN_H  // 2

    best_x  = WIDTH - MARGIN - CARD_W
    score_x = best_x - MARGIN - CARD_W
    btn_x   = score_x - MARGIN - BTN_W

    draw_score_card(window, "BEST",  best_score, best_x,  card_y, CARD_W, CARD_H)
    draw_score_card(window, "SCORE", score,      score_x, card_y, CARD_W, CARD_H)

    btn.rect.update(btn_x, btn_y, BTN_W, BTN_H)
    btn.draw(window)


def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT + BOARD_Y
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR,
                         (x, BOARD_Y), (x, BOARD_Y + BOARD_SIZE), OUTLINE_THICKNESS)
    pygame.draw.rect(window, OUTLINE_COLOR,
                     (0, BOARD_Y, WIDTH, BOARD_SIZE), OUTLINE_THICKNESS)


def draw_footer(window):
    window.fill(HEADER_BG, (0, BOARD_Y + BOARD_SIZE, WIDTH, FOOTER_HEIGHT))
    hint = "Arrow Keys / WASD: Move   |   R: Restart   |   Z: Undo"
    text = FONT_FOOTER.render(hint, True, FONT_COLOR)
    window.blit(text, (
        WIDTH  // 2 - text.get_width()  // 2,
        BOARD_Y + BOARD_SIZE + FOOTER_HEIGHT // 2 - text.get_height() // 2,
    ))


def draw(window, tiles, score, best_score, popups, btn):
    window.fill(BACKGROUND_COLOR, (0, BOARD_Y, WIDTH, BOARD_SIZE))
    for tile in tiles.values():
        tile.draw(window)
    draw_grid(window)
    draw_header(window, score, best_score, btn)
    draw_footer(window)
    for p in popups:
        p.draw(window)
    pygame.display.update()


def draw_overlay(window, tiles, score, best_score, btn,
                 bg_color, title_txt, sub_txt):
    draw(window, tiles, score, best_score, [], btn)
    overlay = pygame.Surface((WIDTH, BOARD_SIZE), pygame.SRCALPHA)
    overlay.fill((*bg_color, 160))
    window.blit(overlay, (0, BOARD_Y))
    cx = WIDTH  // 2
    cy = BOARD_Y + BOARD_SIZE // 2
    t = FONT_TITLE.render(title_txt, True, (255, 255, 255))
    s = FONT_MED.render(sub_txt,    True, (255, 255, 255))
    window.blit(t, (cx - t.get_width()//2, cy - 40))
    window.blit(s, (cx - s.get_width()//2, cy + 16))
    pygame.display.update()


def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); raise SystemExit
            if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return


def win_screen(window, tiles, score, best_score, btn):
    draw_overlay(window, tiles, score, best_score, btn,
                 (200, 160, 0), "You Win!", "Press any key to continue")
    wait_for_key()


def game_over_screen(window, tiles, score, best_score, btn):
    draw_overlay(window, tiles, score, best_score, btn,
                 (180, 60, 60), "Game Over", "Press any key to restart")
    wait_for_key()


def get_random_pos(tiles):
    while True:
        r, c = random.randrange(ROWS), random.randrange(COLS)
        if f"{r}{c}" not in tiles:
            return r, c


def generate_tiles():
    tiles = {}
    for _ in range(2):
        r, c = get_random_pos(tiles)
        tiles[f"{r}{c}"] = Tile(2, r, c)
    return tiles


def snapshot(tiles, score):
    snapped = {}
    for k, t in tiles.items():
        nt = Tile(t.value, t.row, t.col)
        nt.x, nt.y = t.x, t.y
        snapped[k] = nt
    return snapped, score


def has_moves(tiles):
    if len(tiles) < 16:
        return True
    for t in tiles.values():
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nb = tiles.get(f"{t.row+dr}{t.col+dc}")
            if nb and nb.value == t.value:
                return True
    return False


def animate_undo(window, current_tiles, target_tiles, score, best_score,
                 popups, btn, clock):
    plan        = []
    ghost_tiles = {}

    for key, tgt in target_tiles.items():
        tx = tgt.col * RECT_WIDTH
        ty = tgt.row * RECT_HEIGHT + BOARD_Y
        if key in current_tiles:
            plan.append((current_tiles[key], tx, ty))
        else:
            nt = Tile(tgt.value, tgt.row, tgt.col)
            nt.x, nt.y = tx, ty
            ghost_tiles[key] = nt

    UNDO_VEL = 18

    still_moving = True
    while still_moving:
        clock.tick(FPS)
        still_moving = False
        for tile, tx, ty in plan:
            dx, dy = tx - tile.x, ty - tile.y
            if abs(dx) > UNDO_VEL or abs(dy) > UNDO_VEL:
                tile.x += UNDO_VEL if dx > 0 else (-UNDO_VEL if dx < 0 else 0)
                tile.y += UNDO_VEL if dy > 0 else (-UNDO_VEL if dy < 0 else 0)
                still_moving = True
            else:
                tile.x, tile.y = tx, ty

        vis = dict(current_tiles)
        vis.update(ghost_tiles)
        for p in popups: p.update()
        popups[:] = [p for p in popups if p.alive]
        draw(window, vis, score, best_score, popups, btn)


def move_tiles(window, tiles, clock, direction, score, best_score, popups, btn):
    updated     = True
    blocks      = set()
    merge_score = [0]

    if direction == "left":
        sort_func      = lambda x: x.col
        reverse        = False
        delta          = (-MOVE_VEL, 0)
        boundary_check = lambda t: t.col == 0
        get_next_tile  = lambda t: tiles.get(f"{t.row}{t.col - 1}")
        merge_check    = lambda t, n: t.x > n.x + MOVE_VEL
        move_check     = lambda t, n: t.x > n.x + RECT_WIDTH + MOVE_VEL
        ceil = True
    elif direction == "right":
        sort_func      = lambda x: x.col
        reverse        = True
        delta          = (MOVE_VEL, 0)
        boundary_check = lambda t: t.col == COLS - 1
        get_next_tile  = lambda t: tiles.get(f"{t.row}{t.col + 1}")
        merge_check    = lambda t, n: t.x < n.x - MOVE_VEL
        move_check     = lambda t, n: t.x + RECT_WIDTH + MOVE_VEL < n.x
        ceil = False
    elif direction == "up":
        sort_func      = lambda x: x.row
        reverse        = False
        delta          = (0, -MOVE_VEL)
        boundary_check = lambda t: t.row == 0
        get_next_tile  = lambda t: tiles.get(f"{t.row - 1}{t.col}")
        merge_check    = lambda t, n: t.y > n.y + MOVE_VEL
        move_check     = lambda t, n: t.y > n.y + RECT_HEIGHT + MOVE_VEL
        ceil = True
    elif direction == "down":
        sort_func      = lambda x: x.row
        reverse        = True
        delta          = (0, MOVE_VEL)
        boundary_check = lambda t: t.row == ROWS - 1
        get_next_tile  = lambda t: tiles.get(f"{t.row + 1}{t.col}")
        merge_check    = lambda t, n: t.y < n.y - MOVE_VEL
        move_check     = lambda t, n: t.y + RECT_HEIGHT + MOVE_VEL < n.y
        ceil = False

    while updated:
        clock.tick(FPS)
        updated      = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue
            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif (tile.value == next_tile.value
                  and tile not in blocks and next_tile not in blocks):
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    gained = next_tile.value
                    merge_score[0] += gained
                    px = next_tile.x + RECT_WIDTH  // 2
                    py = next_tile.y + RECT_HEIGHT // 2
                    popups.append(ScorePopup(gained, px, py))
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile, next_tile):
                tile.move(delta)
            else:
                continue

            tile.set_pos(ceil)
            updated = True

        for p in popups: p.update()
        popups[:] = [p for p in popups if p.alive]
        update_tiles(window, tiles, sorted_tiles,
                     score + merge_score[0], best_score, popups, btn)

    score += merge_score[0]
    return end_move(tiles), score


def end_move(tiles):
    if len(tiles) == 16:
        return "lost"
    r, c = get_random_pos(tiles)
    tiles[f"{r}{c}"] = Tile(random.choice([2, 4]), r, c)
    return "continue"


def update_tiles(window, tiles, sorted_tiles, score, best_score, popups, btn):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile
    draw(window, tiles, score, best_score, popups, btn)


def check_win(tiles):
    return any(t.value >= 2048 for t in tiles.values())


def main(window):
    clock      = pygame.time.Clock()
    run        = True
    won        = False
    score      = 0
    best_score = load_highscore()
    tiles      = generate_tiles()
    popups     = []
    history    = []

    btn = Button(0, 0, 86, 34, "New Game")

    def do_restart():
        nonlocal tiles, score, won
        tiles = generate_tiles()
        score = 0
        won   = False
        history.clear()
        popups.clear()

    def push_history():
        history.append(snapshot(tiles, score))
        if len(history) > 10:
            history.pop(0)

    def do_undo():
        nonlocal tiles, score
        if not history:
            return
        target_tiles, target_score = history.pop()
        animate_undo(window, tiles, target_tiles, target_score,
                     best_score, popups, btn, clock)
        tiles = target_tiles
        score = target_score

    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        btn.check_hover(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False; break

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn.is_clicked(mouse_pos):
                    do_restart()

            if event.type == pygame.KEYDOWN:
                direction = None
                if   event.key in (pygame.K_LEFT,  pygame.K_a): direction = "left"
                elif event.key in (pygame.K_RIGHT, pygame.K_d): direction = "right"
                elif event.key in (pygame.K_UP,    pygame.K_w): direction = "up"
                elif event.key in (pygame.K_DOWN,  pygame.K_s): direction = "down"
                elif event.key == pygame.K_r: do_restart()
                elif event.key == pygame.K_z: do_undo()

                if direction:
                    push_history()
                    result, score = move_tiles(
                        window, tiles, clock, direction,
                        score, best_score, popups, btn)

                    if score > best_score:
                        best_score = score
                        save_highscore(best_score)

                    if not won and check_win(tiles):
                        won = True
                        win_screen(window, tiles, score, best_score, btn)

                    if result == "lost" or not has_moves(tiles):
                        game_over_screen(window, tiles, score, best_score, btn)
                        do_restart()

        for p in popups: p.update()
        popups[:] = [p for p in popups if p.alive]
        draw(window, tiles, score, best_score, popups, btn)

    save_highscore(best_score)
    pygame.quit()


if __name__ == "__main__":
    main(WINDOW)
