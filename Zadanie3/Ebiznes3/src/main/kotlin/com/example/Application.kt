package com.example

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.request.*
import io.ktor.server.routing.*
import dev.kord.core.Kord
import dev.kord.common.entity.Snowflake
import dev.kord.core.entity.channel.TextChannel
import dev.kord.core.event.message.MessageCreateEvent
import dev.kord.core.on
import dev.kord.gateway.Intent
import dev.kord.gateway.PrivilegedIntent


suspend fun main() {

    val kord = Kord(System.getenv("TokenDiscord"))
    val id = "1222471804329918528"
    val channel = kord.getChannelOf<TextChannel>(Snowflake(id))
    val categories = listOf("ssaki", "ryby", "ptaki", "gady", "plazy")

    embeddedServer(Netty, host = "127.0.0.1", port = 8080) {
        routing {
            post("/dsc") {
                channel?.createMessage(call.receive<String>())
            }
        }
    }.start(wait = false)

    kord.on<MessageCreateEvent> {

        println(message.author?.username)
        println(message.content)
        if (message.author?.isBot != false) return@on
        if (message.content != "!categories") return@on
        message.channel.createMessage(categories.toString())
    }

    kord.login {
        @OptIn(PrivilegedIntent::class)
        intents += Intent.MessageContent
    }
}

