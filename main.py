def on_a_pressed():
    global t_iraaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooooooo
    t_iraaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooooooo = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . 1 9 7 1 . . . . . . 1 7 9 1 . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        f_ugueteeeeeeeeeeeeeeeeeeee,
        0,
        -150)
    t_iraaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooooooo.start_effect(effects.warm_radial, 500)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite2):
    otherSprite2.destroy(effects.disintegrate)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
t_iraaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooooooo: Sprite = None
f_ugueteeeeeeeeeeeeeeeeeeee: Sprite = None
m_eteoros = [img("""
        . . . . . . . . . c c 8 . . . . 
            . . . . . . 8 c c c f 8 c c . . 
            . . . c c 8 8 f c a f f f c c . 
            . . c c c f f f c a a f f c c c 
            8 c c c f f f f c c a a c 8 c c 
            c c c b f f f 8 a c c a a a c c 
            c a a b b 8 a b c c c c c c c c 
            a f c a a b b a c c c c c f f c 
            a 8 f c a a c c a c a c f f f c 
            c a 8 a a c c c c a a f f f 8 a 
            . a c a a c f f a a b 8 f f c a 
            . . c c b a f f f a b b c c 6 c 
            . . . c b b a f f 6 6 a b 6 c . 
            . . . c c b b b 6 6 a c c c c . 
            . . . . c c a b b c c c . . . . 
            . . . . . c c c c c c . . . . .
    """),
    img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . c c c c . . 
            . c c c c c . c c c c c f c c . 
            c c a c c c c c 8 f f c f f c c 
            c a f a a c c a f f c a a f f c 
            c a 8 f a a c a c c c a a a a c 
            c b c f a a a a a c c c c c c c 
            c b b a a c f 8 a c c c 8 c c c 
            . c b b a b c f a a a 8 8 c c . 
            . . . . a a b b b a a 8 a c . . 
            . . . . c b c a a c c b . . . . 
            . . . . b b c c a b b a . . . . 
            . . . . b b a b a 6 a . . . . . 
            . . . . c b b b 6 6 c . . . . . 
            . . . . . c a 6 6 b c . . . . . 
            . . . . . . . c c c . . . . . .
    """),
    img("""
        . . . . . . c c c . . . . . . . 
            . . . . . a a a c c c . . . . . 
            . . . c a c f a a a a c . . . . 
            . . c a c f f f a f f a c . . . 
            . c c a c c f a a c f f a c . . 
            . a b a a c 6 a a c c f a c c c 
            . a b b b 6 a b b a a c a f f c 
            . . a b b a f f b b a a c f f c 
            c . a a a c c f c b a a c f a c 
            c c a a a c c a a a b b a c a c 
            a c a b b a a 6 a b b 6 b b c . 
            b a c b b b 6 b c . c c a c . . 
            b a c c a b b a c . . . . . . . 
            b b a c a b a a . . . . . . . . 
            a b 6 b b a c . . . . . . . . . 
            . a a b c . . . . . . . . . . .
    """),
    img("""
        . . . . . . . . c c c c . . . . 
            . . . . c c c c c c c c c . . . 
            . . . c f c c a a a a c a c . . 
            . . c c f f f f a a a c a a c . 
            . . c c a f f c a a f f f a a c 
            . . c c a a a a b c f f f a a c 
            . c c c c a c c b a f c a a c c 
            c a f f c c c a b b 6 b b b c c 
            c a f f f f c c c 6 b b b a a c 
            c a a c f f c a 6 6 b b b a a c 
            c c b a a a a b 6 b b a b b a . 
            . c c b b b b b b b a c c b a . 
            . . c c c b c c c b a a b c . . 
            . . . . c b a c c b b b c . . . 
            . . . . c b b a a 6 b c . . . . 
            . . . . . . b 6 6 c c . . . . .
    """)]
f_ugueteeeeeeeeeeeeeeeeeeee = sprites.create(img("""
        ........................
            ..........f.............
            .........fff............
            ........fffff...........
            ........ff1ff...........
            ........ff1ff...........
            .......fff1fff..........
            .......ff111ff..........
            ......fff111fff.........
            .....fff11111fff........
            .....ff1111111ff........
            ....fff1999991fff.......
            ....ff119999991ff.......
            ....ff119999991ff.......
            ...ff11199999911ff......
            ...ff11199999911ff......
            ...ff11199999911ff......
            ...ff11111111111ff......
            ...fffffffffffffff......
            ...22...2552....22......
            ...22.2224422...22......
            ...22.25444522..22......
            ...22.25444552..22......
            ..222.22222222..222.....
    """),
    SpriteKind.player)
scene.set_background_color(0)
f_ugueteeeeeeeeeeeeeeeeeeee.bottom = 120
f_ugueteeeeeeeeeeeeeeeeeeee.set_stay_in_screen(True)
controller.move_sprite(f_ugueteeeeeeeeeeeeeeeeeeee, 100, 0)
effects.star_field.start_screen_effect()
info.set_life(1000000)

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(m_eteoros[randint(0, len(m_eteoros) - 1)], 0, 150)
    projectile.x = randint(0, 160)
game.on_update_interval(500, on_update_interval)
