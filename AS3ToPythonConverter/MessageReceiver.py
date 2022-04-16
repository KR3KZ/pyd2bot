from com.ankamagames.dofus.network.messages.authorized.ConsoleCommandsListMessage import (
    ConsoleCommandsListMessage,
)
from com.ankamagames.dofus.network.messages.authorized.ConsoleMessage import (
    ConsoleMessage,
)
from com.ankamagames.dofus.network.messages.common.NetworkDataContainerMessage import (
    NetworkDataContainerMessage,
)
from com.ankamagames.dofus.network.messages.common.basic.BasicPongMessage import (
    BasicPongMessage,
)
from com.ankamagames.dofus.network.messages.connection.CredentialsAcknowledgementMessage import (
    CredentialsAcknowledgementMessage,
)
from com.ankamagames.dofus.network.messages.connection.HelloConnectMessage import (
    HelloConnectMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationFailedBannedMessage import (
    IdentificationFailedBannedMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationFailedForBadVersionMessage import (
    IdentificationFailedForBadVersionMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import (
    IdentificationFailedMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessMessage import (
    IdentificationSuccessMessage,
)
from com.ankamagames.dofus.network.messages.connection.IdentificationSuccessWithLoginTokenMessage import (
    IdentificationSuccessWithLoginTokenMessage,
)
from com.ankamagames.dofus.network.messages.connection.MigratedServerListMessage import (
    MigratedServerListMessage,
)
from com.ankamagames.dofus.network.messages.connection.SelectedServerDataExtendedMessage import (
    SelectedServerDataExtendedMessage,
)
from com.ankamagames.dofus.network.messages.connection.SelectedServerDataMessage import (
    SelectedServerDataMessage,
)
from com.ankamagames.dofus.network.messages.connection.SelectedServerRefusedMessage import (
    SelectedServerRefusedMessage,
)
from com.ankamagames.dofus.network.messages.connection.ServerStatusUpdateMessage import (
    ServerStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.connection.ServersListMessage import (
    ServersListMessage,
)
from com.ankamagames.dofus.network.messages.connection.register.AccountLinkRequiredMessage import (
    AccountLinkRequiredMessage,
)
from com.ankamagames.dofus.network.messages.connection.register.NicknameAcceptedMessage import (
    NicknameAcceptedMessage,
)
from com.ankamagames.dofus.network.messages.connection.register.NicknameRefusedMessage import (
    NicknameRefusedMessage,
)
from com.ankamagames.dofus.network.messages.connection.register.NicknameRegistrationMessage import (
    NicknameRegistrationMessage,
)
from com.ankamagames.dofus.network.messages.connection.search.AcquaintanceSearchErrorMessage import (
    AcquaintanceSearchErrorMessage,
)
from com.ankamagames.dofus.network.messages.connection.search.AcquaintanceServerListMessage import (
    AcquaintanceServerListMessage,
)
from com.ankamagames.dofus.network.messages.debug.DebugClearHighlightCellsMessage import (
    DebugClearHighlightCellsMessage,
)
from com.ankamagames.dofus.network.messages.debug.DebugHighlightCellsMessage import (
    DebugHighlightCellsMessage,
)
from com.ankamagames.dofus.network.messages.debug.DebugInClientMessage import (
    DebugInClientMessage,
)
from com.ankamagames.dofus.network.messages.debug.DumpedEntityStatsMessage import (
    DumpedEntityStatsMessage,
)
from com.ankamagames.dofus.network.messages.game.PaginationAnswerAbstractMessage import (
    PaginationAnswerAbstractMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementAlmostFinishedDetailedListMessage import (
    AchievementAlmostFinishedDetailedListMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementDetailedListMessage import (
    AchievementDetailedListMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementDetailsMessage import (
    AchievementDetailsMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedInformationMessage import (
    AchievementFinishedInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedMessage import (
    AchievementFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementListMessage import (
    AchievementListMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementRewardErrorMessage import (
    AchievementRewardErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.AchievementRewardSuccessMessage import (
    AchievementRewardSuccessMessage,
)
from com.ankamagames.dofus.network.messages.game.achievement.FriendGuildWarnOnAchievementCompleteStateMessage import (
    FriendGuildWarnOnAchievementCompleteStateMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import (
    AbstractGameActionMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionWithAckMessage import (
    AbstractGameActionWithAckMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.GameActionNoopMessage import (
    GameActionNoopMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.GameActionSpamMessage import (
    GameActionSpamMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.AbstractGameActionFightTargetedAbilityMessage import (
    AbstractGameActionFightTargetedAbilityMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightActivateGlyphTrapMessage import (
    GameActionFightActivateGlyphTrapMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightCarryCharacterMessage import (
    GameActionFightCarryCharacterMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightChangeLookMessage import (
    GameActionFightChangeLookMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightCloseCombatMessage import (
    GameActionFightCloseCombatMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDeathMessage import (
    GameActionFightDeathMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellEffectMessage import (
    GameActionFightDispellEffectMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellMessage import (
    GameActionFightDispellMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellSpellMessage import (
    GameActionFightDispellSpellMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDispellableEffectMessage import (
    GameActionFightDispellableEffectMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDodgePointLossMessage import (
    GameActionFightDodgePointLossMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightDropCharacterMessage import (
    GameActionFightDropCharacterMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightExchangePositionsMessage import (
    GameActionFightExchangePositionsMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightInvisibilityMessage import (
    GameActionFightInvisibilityMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightInvisibleDetectedMessage import (
    GameActionFightInvisibleDetectedMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightKillMessage import (
    GameActionFightKillMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifeAndShieldPointsLostMessage import (
    GameActionFightLifeAndShieldPointsLostMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsGainMessage import (
    GameActionFightLifePointsGainMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightLifePointsLostMessage import (
    GameActionFightLifePointsLostMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightMarkCellsMessage import (
    GameActionFightMarkCellsMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightModifyEffectsDurationMessage import (
    GameActionFightModifyEffectsDurationMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightMultipleSummonMessage import (
    GameActionFightMultipleSummonMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightNoSpellCastMessage import (
    GameActionFightNoSpellCastMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightPointsVariationMessage import (
    GameActionFightPointsVariationMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightReduceDamagesMessage import (
    GameActionFightReduceDamagesMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightReflectDamagesMessage import (
    GameActionFightReflectDamagesMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightReflectSpellMessage import (
    GameActionFightReflectSpellMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightSlideMessage import (
    GameActionFightSlideMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightSpellCastMessage import (
    GameActionFightSpellCastMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightSpellCooldownVariationMessage import (
    GameActionFightSpellCooldownVariationMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightSpellImmunityMessage import (
    GameActionFightSpellImmunityMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightStealKamaMessage import (
    GameActionFightStealKamaMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightSummonMessage import (
    GameActionFightSummonMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightTackledMessage import (
    GameActionFightTackledMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightTeleportOnSameMapMessage import (
    GameActionFightTeleportOnSameMapMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightThrowCharacterMessage import (
    GameActionFightThrowCharacterMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightTriggerEffectMessage import (
    GameActionFightTriggerEffectMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightTriggerGlyphTrapMessage import (
    GameActionFightTriggerGlyphTrapMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightUnmarkCellsMessage import (
    GameActionFightUnmarkCellsMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionFightVanishMessage import (
    GameActionFightVanishMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.fight.GameActionUpdateEffectTriggerCountMessage import (
    GameActionUpdateEffectTriggerCountMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.sequence.SequenceEndMessage import (
    SequenceEndMessage,
)
from com.ankamagames.dofus.network.messages.game.actions.sequence.SequenceStartMessage import (
    SequenceStartMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceBulletinMessage import (
    AllianceBulletinMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceBulletinSetErrorMessage import (
    AllianceBulletinSetErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceCreationResultMessage import (
    AllianceCreationResultMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceCreationStartedMessage import (
    AllianceCreationStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceFactsErrorMessage import (
    AllianceFactsErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceFactsMessage import (
    AllianceFactsMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceGuildLeavingMessage import (
    AllianceGuildLeavingMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceInsiderInfoMessage import (
    AllianceInsiderInfoMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceInvitationStateRecrutedMessage import (
    AllianceInvitationStateRecrutedMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceInvitationStateRecruterMessage import (
    AllianceInvitationStateRecruterMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceInvitedMessage import (
    AllianceInvitedMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceJoinedMessage import (
    AllianceJoinedMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceLeftMessage import (
    AllianceLeftMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceListMessage import (
    AllianceListMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceMembershipMessage import (
    AllianceMembershipMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceModificationStartedMessage import (
    AllianceModificationStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceMotdMessage import (
    AllianceMotdMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AllianceMotdSetErrorMessage import (
    AllianceMotdSetErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.AlliancePartialListMessage import (
    AlliancePartialListMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.KohUpdateMessage import (
    KohUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.alliance.summary.AllianceSummaryMessage import (
    AllianceSummaryMessage,
)
from com.ankamagames.dofus.network.messages.game.almanach.AlmanachCalendarDateMessage import (
    AlmanachCalendarDateMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AccountCapabilitiesMessage import (
    AccountCapabilitiesMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AccountLoggingKickedMessage import (
    AccountLoggingKickedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AlreadyConnectedMessage import (
    AlreadyConnectedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketAcceptedMessage import (
    AuthenticationTicketAcceptedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.AuthenticationTicketRefusedMessage import (
    AuthenticationTicketRefusedMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.HelloGameMessage import (
    HelloGameMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.ReloginTokenStatusMessage import (
    ReloginTokenStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.ServerOptionalFeaturesMessage import (
    ServerOptionalFeaturesMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.ServerSessionConstantsMessage import (
    ServerSessionConstantsMessage,
)
from com.ankamagames.dofus.network.messages.game.approach.ServerSettingsMessage import (
    ServerSettingsMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.AtlasPointInformationsMessage import (
    AtlasPointInformationsMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassResetMessage import (
    CompassResetMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import (
    CompassUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdatePartyMemberMessage import (
    CompassUpdatePartyMemberMessage,
)
from com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdatePvpSeekMessage import (
    CompassUpdatePvpSeekMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicAckMessage import (
    BasicAckMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicDateMessage import (
    BasicDateMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicLatencyStatsRequestMessage import (
    BasicLatencyStatsRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicNoOperationMessage import (
    BasicNoOperationMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicTimeMessage import (
    BasicTimeMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicWhoIsMessage import (
    BasicWhoIsMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.BasicWhoIsNoMatchMessage import (
    BasicWhoIsNoMatchMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.CurrentServerStatusUpdateMessage import (
    CurrentServerStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.NumericWhoIsMessage import (
    NumericWhoIsMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.SequenceNumberRequestMessage import (
    SequenceNumberRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.basic.TextInformationMessage import (
    TextInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.character.alignment.war.effort.AlignmentWarEffortDonatePreviewMessage import (
    AlignmentWarEffortDonatePreviewMessage,
)
from com.ankamagames.dofus.network.messages.game.character.alignment.war.effort.AlignmentWarEffortDonationResultMessage import (
    AlignmentWarEffortDonationResultMessage,
)
from com.ankamagames.dofus.network.messages.game.character.alignment.war.effort.CharacterAlignmentWarEffortProgressionMessage import (
    CharacterAlignmentWarEffortProgressionMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.BasicCharactersListMessage import (
    BasicCharactersListMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedErrorMessage import (
    CharacterSelectedErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedForceMessage import (
    CharacterSelectedForceMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharacterSelectedSuccessMessage import (
    CharacterSelectedSuccessMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListErrorMessage import (
    CharactersListErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListMessage import (
    CharactersListMessage,
)
from com.ankamagames.dofus.network.messages.game.character.choice.CharactersListWithRemodelingMessage import (
    CharactersListWithRemodelingMessage,
)
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterCanBeCreatedResultMessage import (
    CharacterCanBeCreatedResultMessage,
)
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterCreationResultMessage import (
    CharacterCreationResultMessage,
)
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterNameSuggestionFailureMessage import (
    CharacterNameSuggestionFailureMessage,
)
from com.ankamagames.dofus.network.messages.game.character.creation.CharacterNameSuggestionSuccessMessage import (
    CharacterNameSuggestionSuccessMessage,
)
from com.ankamagames.dofus.network.messages.game.character.debt.DebtsDeleteMessage import (
    DebtsDeleteMessage,
)
from com.ankamagames.dofus.network.messages.game.character.debt.DebtsUpdateMessage import (
    DebtsUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.character.deletion.CharacterDeletionErrorMessage import (
    CharacterDeletionErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.character.spell.forgettable.ForgettableSpellDeleteMessage import (
    ForgettableSpellDeleteMessage,
)
from com.ankamagames.dofus.network.messages.game.character.spell.forgettable.ForgettableSpellEquipmentSlotsMessage import (
    ForgettableSpellEquipmentSlotsMessage,
)
from com.ankamagames.dofus.network.messages.game.character.spell.forgettable.ForgettableSpellListUpdateMessage import (
    ForgettableSpellListUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterExperienceGainMessage import (
    CharacterExperienceGainMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpInformationMessage import (
    CharacterLevelUpInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import (
    CharacterLevelUpMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.CharacterStatsListMessage import (
    CharacterStatsListMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.FighterStatsListMessage import (
    FighterStatsListMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.LifePointsRegenBeginMessage import (
    LifePointsRegenBeginMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.LifePointsRegenEndMessage import (
    LifePointsRegenEndMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.UpdateLifePointsMessage import (
    UpdateLifePointsMessage,
)
from com.ankamagames.dofus.network.messages.game.character.stats.UpdateSpellModifierMessage import (
    UpdateSpellModifierMessage,
)
from com.ankamagames.dofus.network.messages.game.character.status.PlayerStatusUpdateErrorMessage import (
    PlayerStatusUpdateErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.character.status.PlayerStatusUpdateMessage import (
    PlayerStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatAbstractServerMessage import (
    ChatAbstractServerMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatAdminServerMessage import (
    ChatAdminServerMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatErrorMessage import (
    ChatErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatKolizeumServerMessage import (
    ChatKolizeumServerMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatServerCopyMessage import (
    ChatServerCopyMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatServerCopyWithObjectMessage import (
    ChatServerCopyWithObjectMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatServerMessage import (
    ChatServerMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.ChatServerWithObjectMessage import (
    ChatServerWithObjectMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.channel.ChannelEnablingChangeMessage import (
    ChannelEnablingChangeMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.channel.EnabledChannelsMessage import (
    EnabledChannelsMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.community.ChatCommunityChannelCommunityMessage import (
    ChatCommunityChannelCommunityMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.smiley.ChatSmileyExtraPackListMessage import (
    ChatSmileyExtraPackListMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.smiley.ChatSmileyMessage import (
    ChatSmileyMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.smiley.LocalizedChatSmileyMessage import (
    LocalizedChatSmileyMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.smiley.MoodSmileyResultMessage import (
    MoodSmileyResultMessage,
)
from com.ankamagames.dofus.network.messages.game.chat.smiley.MoodSmileyUpdateMessage import (
    MoodSmileyUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameCautiousMapMovementMessage import (
    GameCautiousMapMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextCreateErrorMessage import (
    GameContextCreateErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextCreateMessage import (
    GameContextCreateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextDestroyMessage import (
    GameContextDestroyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextMoveElementMessage import (
    GameContextMoveElementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextMoveMultipleElementsMessage import (
    GameContextMoveMultipleElementsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextRefreshEntityLookMessage import (
    GameContextRefreshEntityLookMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementMessage import (
    GameContextRemoveElementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveElementWithEventMessage import (
    GameContextRemoveElementWithEventMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsMessage import (
    GameContextRemoveMultipleElementsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameContextRemoveMultipleElementsWithEventsMessage import (
    GameContextRemoveMultipleElementsWithEventsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntitiesDispositionMessage import (
    GameEntitiesDispositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntityDispositionErrorMessage import (
    GameEntityDispositionErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameEntityDispositionMessage import (
    GameEntityDispositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapChangeOrientationMessage import (
    GameMapChangeOrientationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapChangeOrientationsMessage import (
    GameMapChangeOrientationsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapMovementMessage import (
    GameMapMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapNoMovementMessage import (
    GameMapNoMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameMapSpeedMovementMessage import (
    GameMapSpeedMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.context.GameRefreshMonsterBoostsMessage import (
    GameRefreshMonsterBoostsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import (
    ShowCellMessage,
)
from com.ankamagames.dofus.network.messages.game.context.ShowCellSpectatorMessage import (
    ShowCellSpectatorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.display.DisplayNumericalValuePaddockMessage import (
    DisplayNumericalValuePaddockMessage,
)
from com.ankamagames.dofus.network.messages.game.context.dungeon.DungeonKeyRingMessage import (
    DungeonKeyRingMessage,
)
from com.ankamagames.dofus.network.messages.game.context.dungeon.DungeonKeyRingUpdateMessage import (
    DungeonKeyRingUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightEndMessage import (
    GameFightEndMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightHumanReadyStateMessage import (
    GameFightHumanReadyStateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import (
    GameFightJoinMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightLeaveMessage import (
    GameFightLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightNewRoundMessage import (
    GameFightNewRoundMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightNewWaveMessage import (
    GameFightNewWaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightOptionStateUpdateMessage import (
    GameFightOptionStateUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPauseMessage import (
    GameFightPauseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementPossiblePositionsMessage import (
    GameFightPlacementPossiblePositionsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsCancelledMessage import (
    GameFightPlacementSwapPositionsCancelledMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsErrorMessage import (
    GameFightPlacementSwapPositionsErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsMessage import (
    GameFightPlacementSwapPositionsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightPlacementSwapPositionsOfferMessage import (
    GameFightPlacementSwapPositionsOfferMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightRemoveTeamMemberMessage import (
    GameFightRemoveTeamMemberMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeMessage import (
    GameFightResumeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightResumeWithSlavesMessage import (
    GameFightResumeWithSlavesMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectateMessage import (
    GameFightSpectateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSpectatorJoinMessage import (
    GameFightSpectatorJoinMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightStartMessage import (
    GameFightStartMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightStartingMessage import (
    GameFightStartingMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightSynchronizeMessage import (
    GameFightSynchronizeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnEndMessage import (
    GameFightTurnEndMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnListMessage import (
    GameFightTurnListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnReadyRequestMessage import (
    GameFightTurnReadyRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnResumeMessage import (
    GameFightTurnResumeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartMessage import (
    GameFightTurnStartMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightTurnStartPlayingMessage import (
    GameFightTurnStartPlayingMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.GameFightUpdateTeamMessage import (
    GameFightUpdateTeamMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.RefreshCharacterStatsMessage import (
    RefreshCharacterStatsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.SlaveNoLongerControledMessage import (
    SlaveNoLongerControledMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.SlaveSwitchContextMessage import (
    SlaveSwitchContextMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.arena.ArenaFighterIdleMessage import (
    ArenaFighterIdleMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.arena.ArenaFighterLeaveMessage import (
    ArenaFighterLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.breach.BreachGameFightEndMessage import (
    BreachGameFightEndMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.challenge.ChallengeInfoMessage import (
    ChallengeInfoMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.challenge.ChallengeResultMessage import (
    ChallengeResultMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.challenge.ChallengeTargetUpdateMessage import (
    ChallengeTargetUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.challenge.ChallengeTargetsListMessage import (
    ChallengeTargetsListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightRefreshFighterMessage import (
    GameFightRefreshFighterMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import (
    GameFightShowFighterMessage,
)
from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterRandomStaticPoseMessage import (
    GameFightShowFighterRandomStaticPoseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.GameDataPaddockObjectAddMessage import (
    GameDataPaddockObjectAddMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.GameDataPaddockObjectListAddMessage import (
    GameDataPaddockObjectListAddMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.GameDataPaddockObjectRemoveMessage import (
    GameDataPaddockObjectRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountDataErrorMessage import (
    MountDataErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountDataMessage import (
    MountDataMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountEmoteIconUsedOkMessage import (
    MountEmoteIconUsedOkMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountEquipedErrorMessage import (
    MountEquipedErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountReleasedMessage import (
    MountReleasedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountRenamedMessage import (
    MountRenamedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountRidingMessage import (
    MountRidingMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountSetMessage import (
    MountSetMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountSterilizedMessage import (
    MountSterilizedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountUnSetMessage import (
    MountUnSetMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.MountXpRatioMessage import (
    MountXpRatioMessage,
)
from com.ankamagames.dofus.network.messages.game.context.mount.PaddockBuyResultMessage import (
    PaddockBuyResultMessage,
)
from com.ankamagames.dofus.network.messages.game.context.notification.NotificationByServerMessage import (
    NotificationByServerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.notification.NotificationListMessage import (
    NotificationListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.AnomalySubareaInformationResponseMessage import (
    AnomalySubareaInformationResponseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapInstanceMessage import (
    CurrentMapInstanceMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapMessage import (
    CurrentMapMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.GameRolePlayShowActorMessage import (
    GameRolePlayShowActorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.GameRolePlayShowActorWithEventMessage import (
    GameRolePlayShowActorWithEventMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.GameRolePlayShowMultipleActorsMessage import (
    GameRolePlayShowMultipleActorsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataInHavenBagMessage import (
    MapComplementaryInformationsDataInHavenBagMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataInHouseMessage import (
    MapComplementaryInformationsDataInHouseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import (
    MapComplementaryInformationsDataMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsWithCoordsMessage import (
    MapComplementaryInformationsWithCoordsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapFightCountMessage import (
    MapFightCountMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapFightStartPositionsUpdateMessage import (
    MapFightStartPositionsUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapObstacleUpdateMessage import (
    MapObstacleUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRewardRateMessage import (
    MapRewardRateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightDetailsExtendedMessage import (
    MapRunningFightDetailsExtendedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightDetailsMessage import (
    MapRunningFightDetailsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapRunningFightListMessage import (
    MapRunningFightListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.TeleportOnSameMapMessage import (
    TeleportOnSameMapMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.alignment.war.effort.AlignmentWarEffortProgressionMessage import (
    AlignmentWarEffortProgressionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.anomaly.AnomalyStateMessage import (
    AnomalyStateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.anomaly.MapComplementaryInformationsAnomalyMessage import (
    MapComplementaryInformationsAnomalyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachBonusMessage import (
    BreachBonusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachBudgetMessage import (
    BreachBudgetMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachCharactersMessage import (
    BreachCharactersMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachEnterMessage import (
    BreachEnterMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachExitResponseMessage import (
    BreachExitResponseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachRoomLockedMessage import (
    BreachRoomLockedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachRoomUnlockResultMessage import (
    BreachRoomUnlockResultMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachSavedMessage import (
    BreachSavedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachStateMessage import (
    BreachStateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.BreachTeleportResponseMessage import (
    BreachTeleportResponseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.MapComplementaryInformationsBreachMessage import (
    MapComplementaryInformationsBreachMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.branch.BreachBranchesMessage import (
    BreachBranchesMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.meeting.BreachInvitationCloseMessage import (
    BreachInvitationCloseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.meeting.BreachInvitationOfferMessage import (
    BreachInvitationOfferMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.meeting.BreachInvitationResponseMessage import (
    BreachInvitationResponseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.meeting.BreachKickResponseMessage import (
    BreachKickResponseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.reward.BreachRewardBoughtMessage import (
    BreachRewardBoughtMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.breach.reward.BreachRewardsMessage import (
    BreachRewardsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.death.GameRolePlayGameOverMessage import (
    GameRolePlayGameOverMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.death.GameRolePlayPlayerLifeStatusMessage import (
    GameRolePlayPlayerLifeStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionFinishedMessage import (
    GameRolePlayDelayedActionFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedActionMessage import (
    GameRolePlayDelayedActionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.delay.GameRolePlayDelayedObjectUseMessage import (
    GameRolePlayDelayedObjectUseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.document.DocumentReadingBeginMessage import (
    DocumentReadingBeginMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmoteAddMessage import (
    EmoteAddMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmoteListMessage import (
    EmoteListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayAbstractMessage import (
    EmotePlayAbstractMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayErrorMessage import (
    EmotePlayErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayMassiveMessage import (
    EmotePlayMassiveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmotePlayMessage import (
    EmotePlayMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.emote.EmoteRemoveMessage import (
    EmoteRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayAggressionMessage import (
    GameRolePlayAggressionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayFightRequestCanceledMessage import (
    GameRolePlayFightRequestCanceledMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayMonsterAngryAtPlayerMessage import (
    GameRolePlayMonsterAngryAtPlayerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayMonsterNotAngryAtPlayerMessage import (
    GameRolePlayMonsterNotAngryAtPlayerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayPlayerFightFriendlyAnsweredMessage import (
    GameRolePlayPlayerFightFriendlyAnsweredMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayPlayerFightFriendlyRequestedMessage import (
    GameRolePlayPlayerFightFriendlyRequestedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayRemoveChallengeMessage import (
    GameRolePlayRemoveChallengeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.GameRolePlayShowChallengeMessage import (
    GameRolePlayShowChallengeMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaFightPropositionMessage import (
    GameRolePlayArenaFightPropositionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaFighterStatusMessage import (
    GameRolePlayArenaFighterStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaInvitationCandidatesAnswerMessage import (
    GameRolePlayArenaInvitationCandidatesAnswerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaLeagueRewardsMessage import (
    GameRolePlayArenaLeagueRewardsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaPlayerBehavioursMessage import (
    GameRolePlayArenaPlayerBehavioursMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaRegistrationStatusMessage import (
    GameRolePlayArenaRegistrationStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaRegistrationWarningMessage import (
    GameRolePlayArenaRegistrationWarningMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaSwitchToFightServerMessage import (
    GameRolePlayArenaSwitchToFightServerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaSwitchToGameServerMessage import (
    GameRolePlayArenaSwitchToGameServerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage import (
    GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.fight.arena.GameRolePlayArenaUpdatePlayerInfosMessage import (
    GameRolePlayArenaUpdatePlayerInfosMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.EditHavenBagFinishedMessage import (
    EditHavenBagFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.EditHavenBagStartMessage import (
    EditHavenBagStartMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.HavenBagDailyLoteryMessage import (
    HavenBagDailyLoteryMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.HavenBagFurnituresMessage import (
    HavenBagFurnituresMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.HavenBagPackListMessage import (
    HavenBagPackListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.HavenBagRoomUpdateMessage import (
    HavenBagRoomUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.meeting.HavenBagPermissionsUpdateMessage import (
    HavenBagPermissionsUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.meeting.InviteInHavenBagClosedMessage import (
    InviteInHavenBagClosedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.meeting.InviteInHavenBagMessage import (
    InviteInHavenBagMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.havenbag.meeting.InviteInHavenBagOfferMessage import (
    InviteInHavenBagOfferMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.AccountHouseMessage import (
    AccountHouseMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseBuyResultMessage import (
    HouseBuyResultMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HousePropertiesMessage import (
    HousePropertiesMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseSellingUpdateMessage import (
    HouseSellingUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseToSellListMessage import (
    HouseToSellListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.guild.HouseGuildNoneMessage import (
    HouseGuildNoneMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.guild.HouseGuildRightsMessage import (
    HouseGuildRightsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import (
    JobAllowMultiCraftRequestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobBookSubscriptionMessage import (
    JobBookSubscriptionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobCrafterDirectoryAddMessage import (
    JobCrafterDirectoryAddMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobCrafterDirectoryEntryMessage import (
    JobCrafterDirectoryEntryMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobCrafterDirectoryListMessage import (
    JobCrafterDirectoryListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobCrafterDirectoryRemoveMessage import (
    JobCrafterDirectoryRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobCrafterDirectorySettingsMessage import (
    JobCrafterDirectorySettingsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobDescriptionMessage import (
    JobDescriptionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobExperienceMultiUpdateMessage import (
    JobExperienceMultiUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobExperienceOtherPlayerUpdateMessage import (
    JobExperienceOtherPlayerUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobExperienceUpdateMessage import (
    JobExperienceUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobLevelUpMessage import (
    JobLevelUpMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobMultiCraftAvailableSkillsMessage import (
    JobMultiCraftAvailableSkillsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableCodeResultMessage import (
    LockableCodeResultMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableShowCodeDialogMessage import (
    LockableShowCodeDialogMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateAbstractMessage import (
    LockableStateUpdateAbstractMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateHouseDoorMessage import (
    LockableStateUpdateHouseDoorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.lockable.LockableStateUpdateStorageMessage import (
    LockableStateUpdateStorageMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.AlliancePrismDialogQuestionMessage import (
    AlliancePrismDialogQuestionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.AllianceTaxCollectorDialogQuestionExtendedMessage import (
    AllianceTaxCollectorDialogQuestionExtendedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.EntityTalkMessage import (
    EntityTalkMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.ListMapNpcsQuestStatusUpdateMessage import (
    ListMapNpcsQuestStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcDialogCreationMessage import (
    NpcDialogCreationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcDialogQuestionMessage import (
    NpcDialogQuestionMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcGenericActionFailureMessage import (
    NpcGenericActionFailureMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.PortalDialogCreationMessage import (
    PortalDialogCreationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionBasicMessage import (
    TaxCollectorDialogQuestionBasicMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.npc.TaxCollectorDialogQuestionExtendedMessage import (
    TaxCollectorDialogQuestionExtendedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.objects.ObjectGroundAddedMessage import (
    ObjectGroundAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.objects.ObjectGroundListAddedMessage import (
    ObjectGroundListAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.objects.ObjectGroundRemovedMessage import (
    ObjectGroundRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.objects.ObjectGroundRemovedMultipleMessage import (
    ObjectGroundRemovedMultipleMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.paddock.GameDataPlayFarmObjectAnimationMessage import (
    GameDataPlayFarmObjectAnimationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.paddock.PaddockPropertiesMessage import (
    PaddockPropertiesMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.paddock.PaddockSellBuyDialogMessage import (
    PaddockSellBuyDialogMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.paddock.PaddockToSellListMessage import (
    PaddockToSellListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import (
    AbstractPartyEventMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import (
    AbstractPartyMemberInFightMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import (
    AbstractPartyMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.DungeonPartyFinderAvailableDungeonsMessage import (
    DungeonPartyFinderAvailableDungeonsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.DungeonPartyFinderListenErrorMessage import (
    DungeonPartyFinderListenErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.DungeonPartyFinderRegisterErrorMessage import (
    DungeonPartyFinderRegisterErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.DungeonPartyFinderRegisterSuccessMessage import (
    DungeonPartyFinderRegisterSuccessMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.DungeonPartyFinderRoomContentMessage import (
    DungeonPartyFinderRoomContentMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.DungeonPartyFinderRoomContentUpdateMessage import (
    DungeonPartyFinderRoomContentUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyCancelInvitationNotificationMessage import (
    PartyCancelInvitationNotificationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyCannotJoinErrorMessage import (
    PartyCannotJoinErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyDeletedMessage import (
    PartyDeletedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyFollowStatusUpdateMessage import (
    PartyFollowStatusUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationCancelledForGuestMessage import (
    PartyInvitationCancelledForGuestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDetailsMessage import (
    PartyInvitationDetailsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDungeonDetailsMessage import (
    PartyInvitationDungeonDetailsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDungeonMessage import (
    PartyInvitationDungeonMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationMessage import (
    PartyInvitationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyJoinMessage import (
    PartyJoinMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyKickedByMessage import (
    PartyKickedByMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyLeaderUpdateMessage import (
    PartyLeaderUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyLeaveMessage import (
    PartyLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyLocateMembersMessage import (
    PartyLocateMembersMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyLoyaltyStatusMessage import (
    PartyLoyaltyStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberEjectedMessage import (
    PartyMemberEjectedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberInStandardFightMessage import (
    PartyMemberInStandardFightMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberRemoveMessage import (
    PartyMemberRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyModifiableStatusMessage import (
    PartyModifiableStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyNameSetErrorMessage import (
    PartyNameSetErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyNameUpdateMessage import (
    PartyNameUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyNewGuestMessage import (
    PartyNewGuestMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyNewMemberMessage import (
    PartyNewMemberMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyRefuseInvitationNotificationMessage import (
    PartyRefuseInvitationNotificationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyRestrictedMessage import (
    PartyRestrictedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateLightMessage import (
    PartyUpdateLightMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateMessage import (
    PartyUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.breach.PartyMemberInBreachFightMessage import (
    PartyMemberInBreachFightMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.party.entity.PartyEntityUpdateLightMessage import (
    PartyEntityUpdateLightMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.purchasable.PurchasableDialogMessage import (
    PurchasableDialogMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.FollowedQuestsMessage import (
    FollowedQuestsMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestListMessage import (
    QuestListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestObjectiveValidatedMessage import (
    QuestObjectiveValidatedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStartedMessage import (
    QuestStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepInfoMessage import (
    QuestStepInfoMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepStartedMessage import (
    QuestStepStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestStepValidatedMessage import (
    QuestStepValidatedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestValidatedMessage import (
    QuestValidatedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.WatchQuestListMessage import (
    WatchQuestListMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.quest.WatchQuestStepInfoMessage import (
    WatchQuestStepInfoMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.spell.SpellVariantActivationMessage import (
    SpellVariantActivationMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.stats.StatsUpgradeResultMessage import (
    StatsUpgradeResultMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntAvailableRetryCountUpdateMessage import (
    TreasureHuntAvailableRetryCountUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerFailedMessage import (
    TreasureHuntDigRequestAnswerFailedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntDigRequestAnswerMessage import (
    TreasureHuntDigRequestAnswerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntFinishedMessage import (
    TreasureHuntFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntFlagRequestAnswerMessage import (
    TreasureHuntFlagRequestAnswerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntMessage import (
    TreasureHuntMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntRequestAnswerMessage import (
    TreasureHuntRequestAnswerMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt.TreasureHuntShowLegendaryUIMessage import (
    TreasureHuntShowLegendaryUIMessage,
)
from com.ankamagames.dofus.network.messages.game.context.roleplay.visual.GameRolePlaySpellAnimMessage import (
    GameRolePlaySpellAnimMessage,
)
from com.ankamagames.dofus.network.messages.game.dialog.LeaveDialogMessage import (
    LeaveDialogMessage,
)
from com.ankamagames.dofus.network.messages.game.dialog.PauseDialogMessage import (
    PauseDialogMessage,
)
from com.ankamagames.dofus.network.messages.game.entity.EntitiesInformationMessage import (
    EntitiesInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.entity.EntityInformationMessage import (
    EntityInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.finishmoves.FinishMoveListMessage import (
    FinishMoveListMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.AcquaintanceAddedMessage import (
    AcquaintanceAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.AcquaintancesListMessage import (
    AcquaintancesListMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.ContactAddFailureMessage import (
    ContactAddFailureMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendAddFailureMessage import (
    FriendAddFailureMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendAddedMessage import (
    FriendAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendDeleteResultMessage import (
    FriendDeleteResultMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendStatusShareStateMessage import (
    FriendStatusShareStateMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendUpdateMessage import (
    FriendUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendWarnOnConnectionStateMessage import (
    FriendWarnOnConnectionStateMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendWarnOnLevelGainStateMessage import (
    FriendWarnOnLevelGainStateMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.FriendsListMessage import (
    FriendsListMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.GuildMemberWarnOnConnectionStateMessage import (
    GuildMemberWarnOnConnectionStateMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.IgnoredAddFailureMessage import (
    IgnoredAddFailureMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.IgnoredAddedMessage import (
    IgnoredAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.IgnoredDeleteResultMessage import (
    IgnoredDeleteResultMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.IgnoredListMessage import (
    IgnoredListMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.SpouseInformationsMessage import (
    SpouseInformationsMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.SpouseStatusMessage import (
    SpouseStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.friend.WarnOnPermaDeathStateMessage import (
    WarnOnPermaDeathStateMessage,
)
from com.ankamagames.dofus.network.messages.game.guest.GuestLimitationMessage import (
    GuestLimitationMessage,
)
from com.ankamagames.dofus.network.messages.game.guest.GuestModeMessage import (
    GuestModeMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.ChallengeFightJoinRefusedMessage import (
    ChallengeFightJoinRefusedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildBulletinMessage import (
    GuildBulletinMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildBulletinSetErrorMessage import (
    GuildBulletinSetErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildCreationResultMessage import (
    GuildCreationResultMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildCreationStartedMessage import (
    GuildCreationStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildFactsErrorMessage import (
    GuildFactsErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildFactsMessage import (
    GuildFactsMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildHouseRemoveMessage import (
    GuildHouseRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildHouseUpdateInformationMessage import (
    GuildHouseUpdateInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildHousesInformationMessage import (
    GuildHousesInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInAllianceFactsMessage import (
    GuildInAllianceFactsMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInformationsGeneralMessage import (
    GuildInformationsGeneralMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInformationsMemberUpdateMessage import (
    GuildInformationsMemberUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInformationsMembersMessage import (
    GuildInformationsMembersMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInformationsPaddocksMessage import (
    GuildInformationsPaddocksMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInfosUpgradeMessage import (
    GuildInfosUpgradeMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInvitationStateRecrutedMessage import (
    GuildInvitationStateRecrutedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInvitationStateRecruterMessage import (
    GuildInvitationStateRecruterMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildInvitedMessage import (
    GuildInvitedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildJoinedMessage import (
    GuildJoinedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildLeftMessage import (
    GuildLeftMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildLevelUpMessage import (
    GuildLevelUpMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildListMessage import (
    GuildListMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildMemberLeavingMessage import (
    GuildMemberLeavingMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildMemberOnlineStatusMessage import (
    GuildMemberOnlineStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildMembershipMessage import (
    GuildMembershipMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildModificationStartedMessage import (
    GuildModificationStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildMotdMessage import (
    GuildMotdMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildMotdSetErrorMessage import (
    GuildMotdSetErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildPaddockBoughtMessage import (
    GuildPaddockBoughtMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildPaddockRemovedMessage import (
    GuildPaddockRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildRanksMessage import (
    GuildRanksMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildSummaryMessage import (
    GuildSummaryMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.GuildVersatileInfoListMessage import (
    GuildVersatileInfoListMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildApplicationDeletedMessage import (
    GuildApplicationDeletedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildApplicationIsAnsweredMessage import (
    GuildApplicationIsAnsweredMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildApplicationReceivedMessage import (
    GuildApplicationReceivedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildListApplicationAnswerMessage import (
    GuildListApplicationAnswerMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildListApplicationModifiedMessage import (
    GuildListApplicationModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationAbstractMessage import (
    GuildPlayerApplicationAbstractMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationInformationMessage import (
    GuildPlayerApplicationInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerNoApplicationInformationMessage import (
    GuildPlayerNoApplicationInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.chest.AddListenerOnSynchronizedStorageMessage import (
    AddListenerOnSynchronizedStorageMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.chest.ListenersOfSynchronizedStorageMessage import (
    ListenersOfSynchronizedStorageMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.chest.RemoveListenerOnSynchronizedStorageMessage import (
    RemoveListenerOnSynchronizedStorageMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.logbook.GuildLogbookInformationMessage import (
    GuildLogbookInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.recruitment.GuildRecruitmentInvalidateMessage import (
    GuildRecruitmentInvalidateMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.recruitment.RecruitmentInformationMessage import (
    RecruitmentInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import (
    AbstractTaxCollectorListMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightPlayersEnemiesListMessage import (
    GuildFightPlayersEnemiesListMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightPlayersEnemyRemoveMessage import (
    GuildFightPlayersEnemyRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightPlayersHelpersJoinMessage import (
    GuildFightPlayersHelpersJoinMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightPlayersHelpersLeaveMessage import (
    GuildFightPlayersHelpersLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorAttackedMessage import (
    TaxCollectorAttackedMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorAttackedResultMessage import (
    TaxCollectorAttackedResultMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorErrorMessage import (
    TaxCollectorErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorListMessage import (
    TaxCollectorListMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorMovementAddMessage import (
    TaxCollectorMovementAddMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorMovementMessage import (
    TaxCollectorMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorMovementRemoveMessage import (
    TaxCollectorMovementRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorMovementsOfflineMessage import (
    TaxCollectorMovementsOfflineMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TaxCollectorStateUpdateMessage import (
    TaxCollectorStateUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.guild.tax.TopTaxCollectorListMessage import (
    TopTaxCollectorListMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolFightPreparationUpdateMessage import (
    IdolFightPreparationUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolListMessage import (
    IdolListMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolPartyLostMessage import (
    IdolPartyLostMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolPartyRefreshMessage import (
    IdolPartyRefreshMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolSelectErrorMessage import (
    IdolSelectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.idol.IdolSelectedMessage import (
    IdolSelectedMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.CharacterCapabilitiesMessage import (
    CharacterCapabilitiesMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.CharacterLoadingCompleteMessage import (
    CharacterLoadingCompleteMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.OnConnectionEventMessage import (
    OnConnectionEventMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.ServerExperienceModificatorMessage import (
    ServerExperienceModificatorMessage,
)
from com.ankamagames.dofus.network.messages.game.initialization.SetCharacterRestrictionsMessage import (
    SetCharacterRestrictionsMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveElementUpdatedMessage import (
    InteractiveElementUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveMapUpdateMessage import (
    InteractiveMapUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseEndedMessage import (
    InteractiveUseEndedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseErrorMessage import (
    InteractiveUseErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUsedMessage import (
    InteractiveUsedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.StatedElementUpdatedMessage import (
    StatedElementUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.StatedMapUpdateMessage import (
    StatedMapUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.meeting.TeleportBuddiesMessage import (
    TeleportBuddiesMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.meeting.TeleportBuddiesRequestedMessage import (
    TeleportBuddiesRequestedMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.meeting.TeleportToBuddyCloseMessage import (
    TeleportToBuddyCloseMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.meeting.TeleportToBuddyOfferMessage import (
    TeleportToBuddyOfferMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.zaap.KnownZaapListMessage import (
    KnownZaapListMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.zaap.TeleportDestinationsMessage import (
    TeleportDestinationsMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.zaap.ZaapDestinationsMessage import (
    ZaapDestinationsMessage,
)
from com.ankamagames.dofus.network.messages.game.interactive.zaap.ZaapRespawnUpdatedMessage import (
    ZaapRespawnUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.KamasUpdateMessage import (
    KamasUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.ObjectAveragePricesErrorMessage import (
    ObjectAveragePricesErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.ObjectAveragePricesMessage import (
    ObjectAveragePricesMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.DecraftResultMessage import (
    DecraftResultMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.EvolutiveObjectRecycleResultMessage import (
    EvolutiveObjectRecycleResultMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseBuyResultMessage import (
    ExchangeBidHouseBuyResultMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseGenericItemAddedMessage import (
    ExchangeBidHouseGenericItemAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseGenericItemRemovedMessage import (
    ExchangeBidHouseGenericItemRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseInListAddedMessage import (
    ExchangeBidHouseInListAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseInListRemovedMessage import (
    ExchangeBidHouseInListRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseInListUpdatedMessage import (
    ExchangeBidHouseInListUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseItemAddOkMessage import (
    ExchangeBidHouseItemAddOkMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseItemRemoveOkMessage import (
    ExchangeBidHouseItemRemoveOkMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseUnsoldItemsMessage import (
    ExchangeBidHouseUnsoldItemsMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceForSellerMessage import (
    ExchangeBidPriceForSellerMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import (
    ExchangeBidPriceMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidSearchOkMessage import (
    ExchangeBidSearchOkMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBuyOkMessage import (
    ExchangeBuyOkMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftCountModifiedMessage import (
    ExchangeCraftCountModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftPaymentModifiedMessage import (
    ExchangeCraftPaymentModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMagicWithObjectDescMessage import (
    ExchangeCraftResultMagicWithObjectDescMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import (
    ExchangeCraftResultMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectDescMessage import (
    ExchangeCraftResultWithObjectDescMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectIdMessage import (
    ExchangeCraftResultWithObjectIdMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCrafterJobLevelupMessage import (
    ExchangeCrafterJobLevelupMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeErrorMessage import (
    ExchangeErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeGuildTaxCollectorGetMessage import (
    ExchangeGuildTaxCollectorGetMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeIsReadyMessage import (
    ExchangeIsReadyMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeItemAutoCraftStopedMessage import (
    ExchangeItemAutoCraftStopedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeLeaveMessage import (
    ExchangeLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMoneyMovementInformationMessage import (
    ExchangeMoneyMovementInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountFreeFromPaddockMessage import (
    ExchangeMountFreeFromPaddockMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountStableErrorMessage import (
    ExchangeMountStableErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountSterilizeFromPaddockMessage import (
    ExchangeMountSterilizeFromPaddockMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsPaddockAddMessage import (
    ExchangeMountsPaddockAddMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsPaddockRemoveMessage import (
    ExchangeMountsPaddockRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsStableAddMessage import (
    ExchangeMountsStableAddMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsStableBornAddMessage import (
    ExchangeMountsStableBornAddMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsStableRemoveMessage import (
    ExchangeMountsStableRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsTakenFromPaddockMessage import (
    ExchangeMountsTakenFromPaddockMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectAddedMessage import (
    ExchangeObjectAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import (
    ExchangeObjectMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectsAddedMessage import (
    ExchangeObjectsAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeOfflineSoldItemsMessage import (
    ExchangeOfflineSoldItemsMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeOkMultiCraftMessage import (
    ExchangeOkMultiCraftMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeReplyTaxVendorMessage import (
    ExchangeReplyTaxVendorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import (
    ExchangeRequestedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedTradeMessage import (
    ExchangeRequestedTradeMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeSellOkMessage import (
    ExchangeSellOkMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeShopStockMovementRemovedMessage import (
    ExchangeShopStockMovementRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeShopStockMovementUpdatedMessage import (
    ExchangeShopStockMovementUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeShopStockMultiMovementRemovedMessage import (
    ExchangeShopStockMultiMovementRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeShopStockMultiMovementUpdatedMessage import (
    ExchangeShopStockMultiMovementUpdatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeShopStockStartedMessage import (
    ExchangeShopStockStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftMessage import (
    ExchangeStartOkCraftMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftWithInformationMessage import (
    ExchangeStartOkCraftWithInformationMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkEvolutiveObjectRecycleTradeMessage import (
    ExchangeStartOkEvolutiveObjectRecycleTradeMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkHumanVendorMessage import (
    ExchangeStartOkHumanVendorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkJobIndexMessage import (
    ExchangeStartOkJobIndexMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountMessage import (
    ExchangeStartOkMountMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMountWithOutPaddockMessage import (
    ExchangeStartOkMountWithOutPaddockMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMulticraftCrafterMessage import (
    ExchangeStartOkMulticraftCrafterMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkMulticraftCustomerMessage import (
    ExchangeStartOkMulticraftCustomerMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkNpcShopMessage import (
    ExchangeStartOkNpcShopMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkNpcTradeMessage import (
    ExchangeStartOkNpcTradeMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkRecycleTradeMessage import (
    ExchangeStartOkRecycleTradeMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkRunesTradeMessage import (
    ExchangeStartOkRunesTradeMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidBuyerMessage import (
    ExchangeStartedBidBuyerMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidSellerMessage import (
    ExchangeStartedBidSellerMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import (
    ExchangeStartedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMountStockMessage import (
    ExchangeStartedMountStockMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedTaxCollectorShopMessage import (
    ExchangeStartedTaxCollectorShopMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedWithPodsMessage import (
    ExchangeStartedWithPodsMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedWithStorageMessage import (
    ExchangeStartedWithStorageMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStoppedMessage import (
    ExchangeStoppedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesExchangerDescriptionForUserMessage import (
    ExchangeTypesExchangerDescriptionForUserMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesItemsExchangerDescriptionForUserMessage import (
    ExchangeTypesItemsExchangerDescriptionForUserMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeWaitingResultMessage import (
    ExchangeWaitingResultMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeWeightMessage import (
    ExchangeWeightMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ItemNoMoreAvailableMessage import (
    ItemNoMoreAvailableMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.RecycleResultMessage import (
    RecycleResultMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.UpdateMountCharacteristicsMessage import (
    UpdateMountCharacteristicsMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeKamaModifiedMessage import (
    ExchangeKamaModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeMultiCraftCrafterCanUseHisRessourcesMessage import (
    ExchangeMultiCraftCrafterCanUseHisRessourcesMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectModifiedInBagMessage import (
    ExchangeObjectModifiedInBagMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectModifiedMessage import (
    ExchangeObjectModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectPutInBagMessage import (
    ExchangeObjectPutInBagMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectRemovedFromBagMessage import (
    ExchangeObjectRemovedFromBagMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectRemovedMessage import (
    ExchangeObjectRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectsModifiedMessage import (
    ExchangeObjectsModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangeObjectsRemovedMessage import (
    ExchangeObjectsRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ExchangePodsModifiedMessage import (
    ExchangePodsModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.GoldAddedMessage import (
    GoldAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.InventoryContentMessage import (
    InventoryContentMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.InventoryWeightMessage import (
    InventoryWeightMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.LivingObjectMessageMessage import (
    LivingObjectMessageMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.MimicryObjectAssociatedMessage import (
    MimicryObjectAssociatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.MimicryObjectErrorMessage import (
    MimicryObjectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.MimicryObjectPreviewMessage import (
    MimicryObjectPreviewMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectAddedMessage import (
    ObjectAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectDeletedMessage import (
    ObjectDeletedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectErrorMessage import (
    ObjectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectJobAddedMessage import (
    ObjectJobAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectModifiedMessage import (
    ObjectModifiedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectMovementMessage import (
    ObjectMovementMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectQuantityMessage import (
    ObjectQuantityMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsAddedMessage import (
    ObjectsAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsDeletedMessage import (
    ObjectsDeletedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsQuantityMessage import (
    ObjectsQuantityMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemMessage import (
    ObtainedItemMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemWithBonusMessage import (
    ObtainedItemWithBonusMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.SetUpdateMessage import (
    SetUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociatedMessage import (
    SymbioticObjectAssociatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectErrorMessage import (
    SymbioticObjectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.WatchInventoryContentMessage import (
    WatchInventoryContentMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.WrapperObjectAssociatedMessage import (
    WrapperObjectAssociatedMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.items.WrapperObjectErrorMessage import (
    WrapperObjectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.spells.SpellListMessage import (
    SpellListMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.storage.StorageInventoryContentMessage import (
    StorageInventoryContentMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.storage.StorageKamasUpdateMessage import (
    StorageKamasUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.storage.StorageObjectRemoveMessage import (
    StorageObjectRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.storage.StorageObjectUpdateMessage import (
    StorageObjectUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.storage.StorageObjectsRemoveMessage import (
    StorageObjectsRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.storage.StorageObjectsUpdateMessage import (
    StorageObjectsUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.look.AccessoryPreviewErrorMessage import (
    AccessoryPreviewErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.look.AccessoryPreviewMessage import (
    AccessoryPreviewMessage,
)
from com.ankamagames.dofus.network.messages.game.moderation.PopupWarningClosedMessage import (
    PopupWarningClosedMessage,
)
from com.ankamagames.dofus.network.messages.game.moderation.PopupWarningMessage import (
    PopupWarningMessage,
)
from com.ankamagames.dofus.network.messages.game.modificator.AreaFightModificatorUpdateMessage import (
    AreaFightModificatorUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.InvalidPresetsMessage import (
    InvalidPresetsMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.ItemForPresetUpdateMessage import (
    ItemForPresetUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.PresetDeleteResultMessage import (
    PresetDeleteResultMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.PresetSaveErrorMessage import (
    PresetSaveErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.PresetSavedMessage import (
    PresetSavedMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultMessage import (
    PresetUseResultMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultWithMissingIdsMessage import (
    PresetUseResultWithMissingIdsMessage,
)
from com.ankamagames.dofus.network.messages.game.presets.PresetsMessage import (
    PresetsMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightAddedMessage import (
    PrismFightAddedMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightAttackerAddMessage import (
    PrismFightAttackerAddMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightAttackerRemoveMessage import (
    PrismFightAttackerRemoveMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightDefenderAddMessage import (
    PrismFightDefenderAddMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightDefenderLeaveMessage import (
    PrismFightDefenderLeaveMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightRemovedMessage import (
    PrismFightRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismFightStateUpdateMessage import (
    PrismFightStateUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismInfoCloseMessage import (
    PrismInfoCloseMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismInfoInValidMessage import (
    PrismInfoInValidMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismSetSabotagedRefusedMessage import (
    PrismSetSabotagedRefusedMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismSettingsErrorMessage import (
    PrismSettingsErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismsInfoValidMessage import (
    PrismsInfoValidMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismsListMessage import (
    PrismsListMessage,
)
from com.ankamagames.dofus.network.messages.game.prism.PrismsListUpdateMessage import (
    PrismsListUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.progression.suggestion.ActivitySuggestionsMessage import (
    ActivitySuggestionsMessage,
)
from com.ankamagames.dofus.network.messages.game.pvp.AlignmentRankUpdateMessage import (
    AlignmentRankUpdateMessage,
)
from com.ankamagames.dofus.network.messages.game.pvp.UpdateMapPlayersAgressableStatusMessage import (
    UpdateMapPlayersAgressableStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.pvp.UpdateSelfAgressableStatusMessage import (
    UpdateSelfAgressableStatusMessage,
)
from com.ankamagames.dofus.network.messages.game.script.CinematicMessage import (
    CinematicMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarAddErrorMessage import (
    ShortcutBarAddErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarContentMessage import (
    ShortcutBarContentMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarRefreshMessage import (
    ShortcutBarRefreshMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarRemoveErrorMessage import (
    ShortcutBarRemoveErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarRemovedMessage import (
    ShortcutBarRemovedMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarReplacedMessage import (
    ShortcutBarReplacedMessage,
)
from com.ankamagames.dofus.network.messages.game.shortcut.ShortcutBarSwapErrorMessage import (
    ShortcutBarSwapErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.social.BulletinMessage import (
    BulletinMessage,
)
from com.ankamagames.dofus.network.messages.game.social.ContactLookErrorMessage import (
    ContactLookErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.social.ContactLookMessage import (
    ContactLookMessage,
)
from com.ankamagames.dofus.network.messages.game.social.SocialNoticeMessage import (
    SocialNoticeMessage,
)
from com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetErrorMessage import (
    SocialNoticeSetErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionAddMessage import (
    StartupActionAddMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionFinishedMessage import (
    StartupActionFinishedMessage,
)
from com.ankamagames.dofus.network.messages.game.startup.StartupActionsListMessage import (
    StartupActionsListMessage,
)
from com.ankamagames.dofus.network.messages.game.subscriber.SubscriptionLimitationMessage import (
    SubscriptionLimitationMessage,
)
from com.ankamagames.dofus.network.messages.game.subscriber.SubscriptionZoneMessage import (
    SubscriptionZoneMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.OrnamentGainedMessage import (
    OrnamentGainedMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.OrnamentLostMessage import (
    OrnamentLostMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.OrnamentSelectErrorMessage import (
    OrnamentSelectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.OrnamentSelectedMessage import (
    OrnamentSelectedMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.TitleGainedMessage import (
    TitleGainedMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.TitleLostMessage import (
    TitleLostMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.TitleSelectErrorMessage import (
    TitleSelectErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.TitleSelectedMessage import (
    TitleSelectedMessage,
)
from com.ankamagames.dofus.network.messages.game.tinsel.TitlesAndOrnamentsListMessage import (
    TitlesAndOrnamentsListMessage,
)
from com.ankamagames.dofus.network.messages.game.ui.ClientUIOpenedByObjectMessage import (
    ClientUIOpenedByObjectMessage,
)
from com.ankamagames.dofus.network.messages.game.ui.ClientUIOpenedMessage import (
    ClientUIOpenedMessage,
)
from com.ankamagames.dofus.network.messages.handshake.ProtocolRequired import (
    ProtocolRequired,
)
from com.ankamagames.dofus.network.messages.queues.LoginQueueStatusMessage import (
    LoginQueueStatusMessage,
)
from com.ankamagames.dofus.network.messages.queues.QueueStatusMessage import (
    QueueStatusMessage,
)
from com.ankamagames.dofus.network.messages.secure.TrustStatusMessage import (
    TrustStatusMessage,
)
from com.ankamagames.dofus.network.messages.security.CheckFileRequestMessage import (
    CheckFileRequestMessage,
)
from com.ankamagames.dofus.network.messages.security.RawDataMessage import (
    RawDataMessage,
)
from com.ankamagames.dofus.network.messages.server.basic.SystemMessageDisplayMessage import (
    SystemMessageDisplayMessage,
)
from com.ankamagames.dofus.network.messages.subscription.AccountInformationsUpdateMessage import (
    AccountInformationsUpdateMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiApiKeyMessage import (
    HaapiApiKeyMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiAuthErrorMessage import (
    HaapiAuthErrorMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiBufferListMessage import (
    HaapiBufferListMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiBuyValidationMessage import (
    HaapiBuyValidationMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiConfirmationMessage import (
    HaapiConfirmationMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiSessionMessage import (
    HaapiSessionMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiShopApiKeyMessage import (
    HaapiShopApiKeyMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiTokenMessage import (
    HaapiTokenMessage,
)
from com.ankamagames.dofus.network.messages.web.haapi.HaapiValidationMessage import (
    HaapiValidationMessage,
)
from com.ankamagames.dofus.network.messages.wtf.ClientYouAreDrunkMessage import (
    ClientYouAreDrunkMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.RawDataParser import RawDataParser
from com.ankamagames.jerakine.network.UnpackMode import UnpackMode

logger = Logger(__name__)


class MessageReceiver(RawDataParser):
    _messagesTypes: dict = dict()
    _unpackModes: dict = dict()

    _messagesTypes[2497] = PaginationAnswerAbstractMessage
    _messagesTypes[1490] = NetworkDataContainerMessage
    _messagesTypes[1730] = ProtocolRequired
    _messagesTypes[2055] = LoginQueueStatusMessage
    _messagesTypes[1298] = QueueStatusMessage
    _messagesTypes[806] = ConsoleMessage
    _messagesTypes[6227] = ConsoleCommandsListMessage
    _messagesTypes[6424] = HelloConnectMessage
    _messagesTypes[3514] = CredentialsAcknowledgementMessage
    _messagesTypes[9929] = NicknameRegistrationMessage
    _messagesTypes[4034] = AccountLinkRequiredMessage
    _messagesTypes[7996] = NicknameRefusedMessage
    _messagesTypes[6684] = NicknameAcceptedMessage
    _messagesTypes[6384] = IdentificationSuccessMessage
    _messagesTypes[427] = IdentificationSuccessWithLoginTokenMessage
    _messagesTypes[5766] = IdentificationFailedMessage
    _messagesTypes[4724] = IdentificationFailedBannedMessage
    _messagesTypes[6103] = IdentificationFailedForBadVersionMessage
    _messagesTypes[4863] = ServersListMessage
    _messagesTypes[7668] = ServerStatusUpdateMessage
    _messagesTypes[9579] = SelectedServerDataMessage
    _messagesTypes[7776] = SelectedServerDataExtendedMessage
    _messagesTypes[2315] = SelectedServerRefusedMessage
    _messagesTypes[8412] = AcquaintanceSearchErrorMessage
    _messagesTypes[2372] = AcquaintanceServerListMessage
    _messagesTypes[664] = MigratedServerListMessage
    _messagesTypes[8427] = HelloGameMessage
    _messagesTypes[3733] = AuthenticationTicketAcceptedMessage
    _messagesTypes[7611] = AuthenticationTicketRefusedMessage
    _messagesTypes[6242] = AlreadyConnectedMessage
    _messagesTypes[3647] = AccountLoggingKickedMessage
    _messagesTypes[6325] = ReloginTokenStatusMessage
    _messagesTypes[1715] = ServerSettingsMessage
    _messagesTypes[8249] = ServerSessionConstantsMessage
    _messagesTypes[7447] = ServerOptionalFeaturesMessage
    _messagesTypes[4667] = AccountCapabilitiesMessage
    _messagesTypes[1101] = TrustStatusMessage
    _messagesTypes[6679] = AccountInformationsUpdateMessage
    _messagesTypes[9159] = CheckFileRequestMessage
    _messagesTypes[4473] = RawDataMessage
    _messagesTypes[2329] = StartupActionsListMessage
    _messagesTypes[9405] = StartupActionAddMessage
    _messagesTypes[193] = StartupActionFinishedMessage
    _messagesTypes[6756] = CharacterCanBeCreatedResultMessage
    _messagesTypes[8035] = CharacterCreationResultMessage
    _messagesTypes[3567] = CharacterDeletionErrorMessage
    _messagesTypes[9366] = CharacterNameSuggestionSuccessMessage
    _messagesTypes[527] = CharacterNameSuggestionFailureMessage
    _messagesTypes[3971] = BasicCharactersListMessage
    _messagesTypes[7382] = CharactersListMessage
    _messagesTypes[6666] = CharactersListWithRemodelingMessage
    _messagesTypes[6788] = CharactersListErrorMessage
    _messagesTypes[2878] = CharacterSelectedSuccessMessage
    _messagesTypes[3302] = CharacterSelectedForceMessage
    _messagesTypes[9040] = CharacterSelectedErrorMessage
    _messagesTypes[8260] = PopupWarningMessage
    _messagesTypes[8482] = PopupWarningClosedMessage
    _messagesTypes[4573] = BasicDateMessage
    _messagesTypes[430] = BasicTimeMessage
    _messagesTypes[8752] = AlmanachCalendarDateMessage
    _messagesTypes[6422] = BasicNoOperationMessage
    _messagesTypes[8655] = BasicAckMessage
    _messagesTypes[5519] = SystemMessageDisplayMessage
    _messagesTypes[6875] = TextInformationMessage
    _messagesTypes[2940] = OnConnectionEventMessage
    _messagesTypes[1254] = SetCharacterRestrictionsMessage
    _messagesTypes[7253] = ServerExperienceModificatorMessage
    _messagesTypes[1887] = CharacterCapabilitiesMessage
    _messagesTypes[7874] = CharacterLoadingCompleteMessage
    _messagesTypes[4452] = GameContextCreateMessage
    _messagesTypes[2816] = GameContextCreateErrorMessage
    _messagesTypes[1231] = GameContextDestroyMessage
    _messagesTypes[6877] = GameContextRemoveElementMessage
    _messagesTypes[3528] = GameContextRemoveMultipleElementsMessage
    _messagesTypes[2969] = GameContextRemoveElementWithEventMessage
    _messagesTypes[409] = GameContextRemoveMultipleElementsWithEventsMessage
    _messagesTypes[1110] = GameContextMoveElementMessage
    _messagesTypes[5560] = GameContextMoveMultipleElementsMessage
    _messagesTypes[7169] = GameContextRefreshEntityLookMessage
    _messagesTypes[7714] = GameMapSpeedMovementMessage
    _messagesTypes[6929] = GameMapNoMovementMessage
    _messagesTypes[9191] = GameMapMovementMessage
    _messagesTypes[9601] = GameCautiousMapMovementMessage
    _messagesTypes[1116] = GameMapChangeOrientationMessage
    _messagesTypes[3831] = GameMapChangeOrientationsMessage
    _messagesTypes[64] = GameEntityDispositionMessage
    _messagesTypes[3000] = GameEntitiesDispositionMessage
    _messagesTypes[9395] = GameEntityDispositionErrorMessage
    _messagesTypes[8657] = GameRefreshMonsterBoostsMessage
    _messagesTypes[1170] = PlayerStatusUpdateErrorMessage
    _messagesTypes[6964] = PlayerStatusUpdateMessage
    _messagesTypes[3406] = BasicWhoIsMessage
    _messagesTypes[8285] = BasicWhoIsNoMatchMessage
    _messagesTypes[7063] = NumericWhoIsMessage
    _messagesTypes[5303] = BasicPongMessage
    _messagesTypes[1347] = BasicLatencyStatsRequestMessage
    _messagesTypes[3240] = SequenceNumberRequestMessage
    _messagesTypes[38] = CurrentServerStatusUpdateMessage
    _messagesTypes[7716] = CinematicMessage
    _messagesTypes[120] = DumpedEntityStatsMessage
    _messagesTypes[7356] = DebugHighlightCellsMessage
    _messagesTypes[3285] = DebugClearHighlightCellsMessage
    _messagesTypes[2158] = DebugInClientMessage
    _messagesTypes[367] = ClientYouAreDrunkMessage
    _messagesTypes[5321] = DisplayNumericalValuePaddockMessage
    _messagesTypes[3871] = CurrentMapMessage
    _messagesTypes[7813] = CurrentMapInstanceMessage
    _messagesTypes[2720] = TeleportOnSameMapMessage
    _messagesTypes[4675] = MapFightCountMessage
    _messagesTypes[9279] = MapRunningFightListMessage
    _messagesTypes[7296] = MapRunningFightDetailsMessage
    _messagesTypes[6206] = MapRunningFightDetailsExtendedMessage
    _messagesTypes[7517] = MapObstacleUpdateMessage
    _messagesTypes[2203] = MapComplementaryInformationsDataMessage
    _messagesTypes[7853] = MapComplementaryInformationsDataInHouseMessage
    _messagesTypes[8598] = MapComplementaryInformationsWithCoordsMessage
    _messagesTypes[3202] = MapRewardRateMessage
    _messagesTypes[4929] = BreachEnterMessage
    _messagesTypes[2050] = BreachTeleportResponseMessage
    _messagesTypes[7818] = BreachRoomLockedMessage
    _messagesTypes[5488] = BreachRoomUnlockResultMessage
    _messagesTypes[1265] = BreachExitResponseMessage
    _messagesTypes[8282] = MapComplementaryInformationsBreachMessage
    _messagesTypes[1483] = BreachGameFightEndMessage
    _messagesTypes[3282] = AnomalyStateMessage
    _messagesTypes[3607] = MapComplementaryInformationsAnomalyMessage
    _messagesTypes[6534] = MapFightStartPositionsUpdateMessage
    _messagesTypes[6549] = GameRolePlayShowActorMessage
    _messagesTypes[5370] = GameRolePlayShowMultipleActorsMessage
    _messagesTypes[4614] = GameRolePlayShowActorWithEventMessage
    _messagesTypes[5547] = CharacterStatsListMessage
    _messagesTypes[2371] = FighterStatsListMessage
    _messagesTypes[9587] = UpdateSpellModifierMessage
    _messagesTypes[2813] = CharacterLevelUpMessage
    _messagesTypes[1383] = CharacterExperienceGainMessage
    _messagesTypes[9230] = CharacterLevelUpInformationMessage
    _messagesTypes[8920] = UpdateLifePointsMessage
    _messagesTypes[2365] = LifePointsRegenBeginMessage
    _messagesTypes[494] = LifePointsRegenEndMessage
    _messagesTypes[8586] = GameRolePlayPlayerLifeStatusMessage
    _messagesTypes[3701] = GameRolePlayGameOverMessage
    _messagesTypes[9101] = GameRolePlayFightRequestCanceledMessage
    _messagesTypes[1626] = GameRolePlayAggressionMessage
    _messagesTypes[6157] = GameRolePlayPlayerFightFriendlyRequestedMessage
    _messagesTypes[871] = GameRolePlayPlayerFightFriendlyAnsweredMessage
    _messagesTypes[6165] = GameRolePlayArenaRegistrationStatusMessage
    _messagesTypes[1343] = GameRolePlayArenaFightPropositionMessage
    _messagesTypes[9616] = GameRolePlayArenaFighterStatusMessage
    _messagesTypes[9491] = GameRolePlayArenaUpdatePlayerInfosMessage
    _messagesTypes[3033] = GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage
    _messagesTypes[3780] = GameRolePlayArenaSwitchToFightServerMessage
    _messagesTypes[9711] = GameRolePlayArenaSwitchToGameServerMessage
    _messagesTypes[5498] = GameRolePlayArenaInvitationCandidatesAnswerMessage
    _messagesTypes[4959] = GameRolePlayArenaLeagueRewardsMessage
    _messagesTypes[2244] = GameRolePlayArenaPlayerBehavioursMessage
    _messagesTypes[9396] = GameRolePlayArenaRegistrationWarningMessage
    _messagesTypes[8302] = GameRolePlayMonsterAngryAtPlayerMessage
    _messagesTypes[2418] = GameRolePlayMonsterNotAngryAtPlayerMessage
    _messagesTypes[4937] = GameRolePlayShowChallengeMessage
    _messagesTypes[8514] = GameRolePlayRemoveChallengeMessage
    _messagesTypes[6811] = GameRolePlaySpellAnimMessage
    _messagesTypes[7263] = GameRolePlayDelayedActionMessage
    _messagesTypes[1610] = GameRolePlayDelayedObjectUseMessage
    _messagesTypes[9954] = GameRolePlayDelayedActionFinishedMessage
    _messagesTypes[3204] = ShowCellMessage
    _messagesTypes[4547] = ShowCellSpectatorMessage
    _messagesTypes[1407] = GameFightStartingMessage
    _messagesTypes[3603] = GameFightJoinMessage
    _messagesTypes[4519] = GameFightSpectatorJoinMessage
    _messagesTypes[3107] = GameFightPlacementPossiblePositionsMessage
    _messagesTypes[7219] = GameFightPlacementSwapPositionsErrorMessage
    _messagesTypes[8968] = GameFightPlacementSwapPositionsOfferMessage
    _messagesTypes[5655] = GameFightPlacementSwapPositionsCancelledMessage
    _messagesTypes[8732] = GameFightPlacementSwapPositionsMessage
    _messagesTypes[2151] = GameFightOptionStateUpdateMessage
    _messagesTypes[985] = GameFightUpdateTeamMessage
    _messagesTypes[6771] = GameFightRemoveTeamMemberMessage
    _messagesTypes[2605] = GameFightHumanReadyStateMessage
    _messagesTypes[141] = GameFightLeaveMessage
    _messagesTypes[8247] = GameFightStartMessage
    _messagesTypes[6763] = GameFightSpectateMessage
    _messagesTypes[6953] = GameFightResumeMessage
    _messagesTypes[1683] = GameFightResumeWithSlavesMessage
    _messagesTypes[1798] = GameFightEndMessage
    _messagesTypes[9360] = GameFightNewRoundMessage
    _messagesTypes[9689] = GameFightTurnListMessage
    _messagesTypes[575] = GameFightTurnStartMessage
    _messagesTypes[283] = GameFightNewWaveMessage
    _messagesTypes[8349] = GameFightTurnStartPlayingMessage
    _messagesTypes[1695] = GameFightTurnResumeMessage
    _messagesTypes[9521] = GameFightPauseMessage
    _messagesTypes[1189] = SlaveSwitchContextMessage
    _messagesTypes[9600] = SlaveNoLongerControledMessage
    _messagesTypes[8208] = RefreshCharacterStatsMessage
    _messagesTypes[6517] = GameFightTurnReadyRequestMessage
    _messagesTypes[7844] = GameFightSynchronizeMessage
    _messagesTypes[8760] = GameFightTurnEndMessage
    _messagesTypes[3785] = GameFightShowFighterMessage
    _messagesTypes[8487] = GameFightRefreshFighterMessage
    _messagesTypes[3166] = GameFightShowFighterRandomStaticPoseMessage
    _messagesTypes[8201] = ArenaFighterLeaveMessage
    _messagesTypes[5129] = ArenaFighterIdleMessage
    _messagesTypes[1744] = SequenceStartMessage
    _messagesTypes[280] = SequenceEndMessage
    _messagesTypes[9188] = AbstractGameActionMessage
    _messagesTypes[1148] = GameActionNoopMessage
    _messagesTypes[9175] = GameActionSpamMessage
    _messagesTypes[8218] = AbstractGameActionWithAckMessage
    _messagesTypes[5692] = GameActionFightNoSpellCastMessage
    _messagesTypes[1710] = AbstractGameActionFightTargetedAbilityMessage
    _messagesTypes[65] = GameActionFightSpellCastMessage
    _messagesTypes[8107] = GameActionFightCloseCombatMessage
    _messagesTypes[5582] = GameActionUpdateEffectTriggerCountMessage
    _messagesTypes[7986] = GameActionFightInvisibleDetectedMessage
    _messagesTypes[272] = GameActionFightPointsVariationMessage
    _messagesTypes[3891] = GameActionFightTackledMessage
    _messagesTypes[5191] = GameActionFightDeathMessage
    _messagesTypes[5733] = GameActionFightKillMessage
    _messagesTypes[7630] = GameActionFightVanishMessage
    _messagesTypes[1571] = GameActionFightSpellCooldownVariationMessage
    _messagesTypes[7073] = GameActionFightSpellImmunityMessage
    _messagesTypes[5194] = GameActionFightLifePointsGainMessage
    _messagesTypes[3628] = GameActionFightLifePointsLostMessage
    _messagesTypes[894] = GameActionFightLifeAndShieldPointsLostMessage
    _messagesTypes[1706] = GameActionFightDispellableEffectMessage
    _messagesTypes[7760] = GameActionFightReflectSpellMessage
    _messagesTypes[6282] = GameActionFightReduceDamagesMessage
    _messagesTypes[9762] = GameActionFightReflectDamagesMessage
    _messagesTypes[948] = GameActionFightDodgePointLossMessage
    _messagesTypes[2323] = GameActionFightSlideMessage
    _messagesTypes[3745] = GameActionFightTeleportOnSameMapMessage
    _messagesTypes[7475] = GameActionFightExchangePositionsMessage
    _messagesTypes[8988] = GameActionFightDispellMessage
    _messagesTypes[3255] = GameActionFightDispellEffectMessage
    _messagesTypes[6072] = GameActionFightDispellSpellMessage
    _messagesTypes[6083] = GameActionFightModifyEffectsDurationMessage
    _messagesTypes[6678] = GameActionFightTriggerEffectMessage
    _messagesTypes[5660] = GameActionFightStealKamaMessage
    _messagesTypes[250] = GameActionFightChangeLookMessage
    _messagesTypes[2092] = GameActionFightInvisibilityMessage
    _messagesTypes[2897] = GameActionFightSummonMessage
    _messagesTypes[6695] = GameActionFightMultipleSummonMessage
    _messagesTypes[6848] = GameActionFightMarkCellsMessage
    _messagesTypes[8111] = GameActionFightUnmarkCellsMessage
    _messagesTypes[7749] = GameActionFightTriggerGlyphTrapMessage
    _messagesTypes[6444] = GameActionFightActivateGlyphTrapMessage
    _messagesTypes[3830] = GameActionFightCarryCharacterMessage
    _messagesTypes[7724] = GameActionFightThrowCharacterMessage
    _messagesTypes[249] = GameActionFightDropCharacterMessage
    _messagesTypes[1739] = EmoteListMessage
    _messagesTypes[4908] = EmoteAddMessage
    _messagesTypes[8627] = EmoteRemoveMessage
    _messagesTypes[610] = EmotePlayAbstractMessage
    _messagesTypes[792] = EmotePlayMessage
    _messagesTypes[6236] = EmotePlayMassiveMessage
    _messagesTypes[158] = EmotePlayErrorMessage
    _messagesTypes[1197] = ChatSmileyMessage
    _messagesTypes[7168] = ChatCommunityChannelCommunityMessage
    _messagesTypes[5993] = LocalizedChatSmileyMessage
    _messagesTypes[6863] = MoodSmileyResultMessage
    _messagesTypes[6990] = MoodSmileyUpdateMessage
    _messagesTypes[1279] = ChatSmileyExtraPackListMessage
    _messagesTypes[8034] = ChatAbstractServerMessage
    _messagesTypes[373] = ChatServerMessage
    _messagesTypes[1773] = ChatKolizeumServerMessage
    _messagesTypes[6906] = ChatAdminServerMessage
    _messagesTypes[3160] = ChatServerWithObjectMessage
    _messagesTypes[5300] = ChatServerCopyMessage
    _messagesTypes[500] = ChatServerCopyWithObjectMessage
    _messagesTypes[3972] = ChatErrorMessage
    _messagesTypes[9741] = EnabledChannelsMessage
    _messagesTypes[9894] = ChannelEnablingChangeMessage
    _messagesTypes[967] = SpellListMessage
    _messagesTypes[584] = ForgettableSpellListUpdateMessage
    _messagesTypes[3832] = ForgettableSpellDeleteMessage
    _messagesTypes[5735] = ForgettableSpellEquipmentSlotsMessage
    _messagesTypes[5131] = LeaveDialogMessage
    _messagesTypes[6210] = PauseDialogMessage
    _messagesTypes[1751] = InteractiveUseErrorMessage
    _messagesTypes[1847] = InteractiveUsedMessage
    _messagesTypes[4987] = InteractiveUseEndedMessage
    _messagesTypes[8782] = InteractiveMapUpdateMessage
    _messagesTypes[1576] = StatedMapUpdateMessage
    _messagesTypes[322] = InteractiveElementUpdatedMessage
    _messagesTypes[2678] = StatedElementUpdatedMessage
    _messagesTypes[5168] = ZaapRespawnUpdatedMessage
    _messagesTypes[6883] = TeleportDestinationsMessage
    _messagesTypes[4986] = ZaapDestinationsMessage
    _messagesTypes[1272] = KnownZaapListMessage
    _messagesTypes[7478] = TeleportBuddiesMessage
    _messagesTypes[2968] = TeleportBuddiesRequestedMessage
    _messagesTypes[9960] = TeleportToBuddyOfferMessage
    _messagesTypes[332] = TeleportToBuddyCloseMessage
    _messagesTypes[6118] = SpellVariantActivationMessage
    _messagesTypes[99] = StatsUpgradeResultMessage
    _messagesTypes[1506] = ChallengeTargetsListMessage
    _messagesTypes[5420] = ChallengeInfoMessage
    _messagesTypes[748] = ChallengeTargetUpdateMessage
    _messagesTypes[7931] = ChallengeResultMessage
    _messagesTypes[6691] = EntityInformationMessage
    _messagesTypes[4126] = EntitiesInformationMessage
    _messagesTypes[7051] = IdolSelectErrorMessage
    _messagesTypes[2306] = IdolSelectedMessage
    _messagesTypes[5686] = IdolListMessage
    _messagesTypes[2234] = IdolPartyRefreshMessage
    _messagesTypes[4969] = IdolPartyLostMessage
    _messagesTypes[146] = IdolFightPreparationUpdateMessage
    _messagesTypes[9613] = AchievementListMessage
    _messagesTypes[7443] = AchievementDetailsMessage
    _messagesTypes[8447] = AchievementDetailedListMessage
    _messagesTypes[133] = AchievementAlmostFinishedDetailedListMessage
    _messagesTypes[6489] = AchievementFinishedMessage
    _messagesTypes[7708] = AchievementFinishedInformationMessage
    _messagesTypes[6364] = AchievementRewardSuccessMessage
    _messagesTypes[5763] = AchievementRewardErrorMessage
    _messagesTypes[7354] = FriendGuildWarnOnAchievementCompleteStateMessage
    _messagesTypes[8007] = DungeonKeyRingMessage
    _messagesTypes[6572] = DungeonKeyRingUpdateMessage
    _messagesTypes[4601] = UpdateMapPlayersAgressableStatusMessage
    _messagesTypes[1944] = UpdateSelfAgressableStatusMessage
    _messagesTypes[953] = AlignmentRankUpdateMessage
    _messagesTypes[8958] = CompassResetMessage
    _messagesTypes[1473] = CompassUpdateMessage
    _messagesTypes[598] = CompassUpdatePartyMemberMessage
    _messagesTypes[5051] = AtlasPointInformationsMessage
    _messagesTypes[8299] = CompassUpdatePvpSeekMessage
    _messagesTypes[9566] = AbstractPartyMessage
    _messagesTypes[8734] = AbstractPartyEventMessage
    _messagesTypes[9235] = PartyModifiableStatusMessage
    _messagesTypes[7030] = PartyInvitationMessage
    _messagesTypes[2600] = PartyInvitationDungeonMessage
    _messagesTypes[5287] = PartyInvitationDetailsMessage
    _messagesTypes[9163] = PartyInvitationDungeonDetailsMessage
    _messagesTypes[3125] = PartyInvitationCancelledForGuestMessage
    _messagesTypes[9404] = PartyCancelInvitationNotificationMessage
    _messagesTypes[9315] = PartyRefuseInvitationNotificationMessage
    _messagesTypes[1903] = PartyCannotJoinErrorMessage
    _messagesTypes[2640] = PartyJoinMessage
    _messagesTypes[5642] = PartyNewGuestMessage
    _messagesTypes[465] = PartyUpdateMessage
    _messagesTypes[8047] = PartyNewMemberMessage
    _messagesTypes[8058] = PartyUpdateLightMessage
    _messagesTypes[4442] = PartyEntityUpdateLightMessage
    _messagesTypes[7770] = PartyMemberRemoveMessage
    _messagesTypes[1880] = PartyMemberEjectedMessage
    _messagesTypes[1866] = PartyLeaderUpdateMessage
    _messagesTypes[1757] = PartyFollowStatusUpdateMessage
    _messagesTypes[2028] = PartyLocateMembersMessage
    _messagesTypes[1327] = PartyLeaveMessage
    _messagesTypes[2835] = PartyKickedByMessage
    _messagesTypes[4094] = PartyRestrictedMessage
    _messagesTypes[1536] = PartyDeletedMessage
    _messagesTypes[9291] = PartyLoyaltyStatusMessage
    _messagesTypes[1165] = AbstractPartyMemberInFightMessage
    _messagesTypes[4603] = PartyMemberInStandardFightMessage
    _messagesTypes[1630] = PartyMemberInBreachFightMessage
    _messagesTypes[7727] = PartyNameUpdateMessage
    _messagesTypes[4438] = PartyNameSetErrorMessage
    _messagesTypes[1688] = DungeonPartyFinderAvailableDungeonsMessage
    _messagesTypes[336] = DungeonPartyFinderListenErrorMessage
    _messagesTypes[726] = DungeonPartyFinderRoomContentMessage
    _messagesTypes[7648] = DungeonPartyFinderRoomContentUpdateMessage
    _messagesTypes[2977] = DungeonPartyFinderRegisterSuccessMessage
    _messagesTypes[7521] = DungeonPartyFinderRegisterErrorMessage
    _messagesTypes[8667] = ContactAddFailureMessage
    _messagesTypes[2627] = SpouseStatusMessage
    _messagesTypes[4381] = FriendsListMessage
    _messagesTypes[6963] = AcquaintancesListMessage
    _messagesTypes[9621] = SpouseInformationsMessage
    _messagesTypes[9647] = FriendAddFailureMessage
    _messagesTypes[2313] = AcquaintanceAddedMessage
    _messagesTypes[4007] = FriendAddedMessage
    _messagesTypes[7984] = FriendUpdateMessage
    _messagesTypes[7028] = FriendDeleteResultMessage
    _messagesTypes[2872] = FriendWarnOnConnectionStateMessage
    _messagesTypes[6545] = WarnOnPermaDeathStateMessage
    _messagesTypes[2454] = FriendWarnOnLevelGainStateMessage
    _messagesTypes[3877] = FriendStatusShareStateMessage
    _messagesTypes[802] = IgnoredListMessage
    _messagesTypes[9152] = IgnoredAddFailureMessage
    _messagesTypes[4502] = IgnoredAddedMessage
    _messagesTypes[2242] = IgnoredDeleteResultMessage
    _messagesTypes[5968] = AllianceCreationStartedMessage
    _messagesTypes[8279] = AllianceModificationStartedMessage
    _messagesTypes[5159] = AllianceCreationResultMessage
    _messagesTypes[4726] = AllianceInvitedMessage
    _messagesTypes[5885] = AllianceInvitationStateRecruterMessage
    _messagesTypes[9943] = AllianceInvitationStateRecrutedMessage
    _messagesTypes[8742] = AllianceJoinedMessage
    _messagesTypes[5586] = AllianceGuildLeavingMessage
    _messagesTypes[6833] = AllianceLeftMessage
    _messagesTypes[4163] = AllianceMembershipMessage
    _messagesTypes[172] = AllianceSummaryMessage
    _messagesTypes[8188] = KohUpdateMessage
    _messagesTypes[2587] = AreaFightModificatorUpdateMessage
    _messagesTypes[4363] = ClientUIOpenedMessage
    _messagesTypes[9520] = ClientUIOpenedByObjectMessage
    _messagesTypes[7468] = GuildLogbookInformationMessage
    _messagesTypes[912] = GuildSummaryMessage
    _messagesTypes[9948] = GuildCreationStartedMessage
    _messagesTypes[4342] = GuildModificationStartedMessage
    _messagesTypes[7696] = GuildCreationResultMessage
    _messagesTypes[9234] = GuildInvitedMessage
    _messagesTypes[2787] = GuildInvitationStateRecruterMessage
    _messagesTypes[3106] = GuildInvitationStateRecrutedMessage
    _messagesTypes[2641] = GuildJoinedMessage
    _messagesTypes[4229] = GuildMemberOnlineStatusMessage
    _messagesTypes[3873] = GuildInformationsGeneralMessage
    _messagesTypes[6736] = GuildInformationsMembersMessage
    _messagesTypes[2768] = GuildInformationsMemberUpdateMessage
    _messagesTypes[1386] = GuildInformationsPaddocksMessage
    _messagesTypes[6137] = GuildMemberLeavingMessage
    _messagesTypes[3734] = GuildLeftMessage
    _messagesTypes[2565] = GuildMembershipMessage
    _messagesTypes[3477] = GuildLevelUpMessage
    _messagesTypes[9899] = GuildInfosUpgradeMessage
    _messagesTypes[5298] = GuildHousesInformationMessage
    _messagesTypes[5248] = GuildHouseUpdateInformationMessage
    _messagesTypes[1663] = GuildHouseRemoveMessage
    _messagesTypes[5835] = GuildPaddockBoughtMessage
    _messagesTypes[3096] = GuildPaddockRemovedMessage
    _messagesTypes[5224] = GuildMemberWarnOnConnectionStateMessage
    _messagesTypes[5546] = GuildMotdMessage
    _messagesTypes[7761] = GuildMotdSetErrorMessage
    _messagesTypes[131] = GuildBulletinMessage
    _messagesTypes[4748] = GuildBulletinSetErrorMessage
    _messagesTypes[3499] = GuildFactsErrorMessage
    _messagesTypes[1750] = GuildFactsMessage
    _messagesTypes[3808] = GuildInAllianceFactsMessage
    _messagesTypes[1680] = GuildRanksMessage
    _messagesTypes[6181] = AllianceFactsErrorMessage
    _messagesTypes[7769] = AllianceFactsMessage
    _messagesTypes[3993] = GuildListMessage
    _messagesTypes[6214] = GuildVersatileInfoListMessage
    _messagesTypes[8557] = AllianceListMessage
    _messagesTypes[822] = AlliancePartialListMessage
    _messagesTypes[1950] = AllianceInsiderInfoMessage
    _messagesTypes[9564] = AllianceMotdMessage
    _messagesTypes[2004] = AllianceMotdSetErrorMessage
    _messagesTypes[661] = AllianceBulletinMessage
    _messagesTypes[3851] = AllianceBulletinSetErrorMessage
    _messagesTypes[4091] = TaxCollectorMovementMessage
    _messagesTypes[4973] = TaxCollectorErrorMessage
    _messagesTypes[1669] = AbstractTaxCollectorListMessage
    _messagesTypes[2693] = TaxCollectorListMessage
    _messagesTypes[448] = TopTaxCollectorListMessage
    _messagesTypes[2951] = TaxCollectorStateUpdateMessage
    _messagesTypes[6849] = TaxCollectorMovementAddMessage
    _messagesTypes[4853] = TaxCollectorMovementRemoveMessage
    _messagesTypes[8771] = TaxCollectorAttackedMessage
    _messagesTypes[6617] = TaxCollectorAttackedResultMessage
    _messagesTypes[8503] = GuildFightPlayersHelpersJoinMessage
    _messagesTypes[6244] = GuildFightPlayersHelpersLeaveMessage
    _messagesTypes[2719] = GuildFightPlayersEnemiesListMessage
    _messagesTypes[9870] = GuildFightPlayersEnemyRemoveMessage
    _messagesTypes[6816] = TaxCollectorMovementsOfflineMessage
    _messagesTypes[9761] = RecruitmentInformationMessage
    _messagesTypes[6055] = GuildRecruitmentInvalidateMessage
    _messagesTypes[2156] = GuildApplicationDeletedMessage
    _messagesTypes[816] = GuildPlayerApplicationAbstractMessage
    _messagesTypes[1200] = GuildPlayerApplicationInformationMessage
    _messagesTypes[2644] = GuildPlayerNoApplicationInformationMessage
    _messagesTypes[3119] = GuildApplicationIsAnsweredMessage
    _messagesTypes[169] = GuildListApplicationAnswerMessage
    _messagesTypes[4943] = GuildListApplicationModifiedMessage
    _messagesTypes[8561] = GuildApplicationReceivedMessage
    _messagesTypes[8019] = ListenersOfSynchronizedStorageMessage
    _messagesTypes[4465] = AddListenerOnSynchronizedStorageMessage
    _messagesTypes[107] = RemoveListenerOnSynchronizedStorageMessage
    _messagesTypes[4808] = PrismSetSabotagedRefusedMessage
    _messagesTypes[3949] = PrismFightDefenderAddMessage
    _messagesTypes[8021] = PrismFightDefenderLeaveMessage
    _messagesTypes[5938] = PrismFightAttackerAddMessage
    _messagesTypes[3537] = PrismFightAttackerRemoveMessage
    _messagesTypes[9789] = PrismsListMessage
    _messagesTypes[7086] = PrismsListUpdateMessage
    _messagesTypes[4862] = ChallengeFightJoinRefusedMessage
    _messagesTypes[3902] = PrismInfoCloseMessage
    _messagesTypes[4883] = PrismsInfoValidMessage
    _messagesTypes[8522] = PrismFightAddedMessage
    _messagesTypes[4052] = PrismFightRemovedMessage
    _messagesTypes[8239] = PrismInfoInValidMessage
    _messagesTypes[9539] = PrismFightStateUpdateMessage
    _messagesTypes[7997] = PrismSettingsErrorMessage
    _messagesTypes[4672] = QuestListMessage
    _messagesTypes[3205] = QuestStartedMessage
    _messagesTypes[6536] = QuestValidatedMessage
    _messagesTypes[5846] = QuestObjectiveValidatedMessage
    _messagesTypes[3032] = QuestStepValidatedMessage
    _messagesTypes[3639] = QuestStepStartedMessage
    _messagesTypes[6202] = QuestStepInfoMessage
    _messagesTypes[1779] = FollowedQuestsMessage
    _messagesTypes[1802] = WatchQuestStepInfoMessage
    _messagesTypes[3233] = WatchQuestListMessage
    _messagesTypes[1912] = NotificationListMessage
    _messagesTypes[9779] = NotificationByServerMessage
    _messagesTypes[7869] = SubscriptionLimitationMessage
    _messagesTypes[5068] = SubscriptionZoneMessage
    _messagesTypes[8462] = GuestLimitationMessage
    _messagesTypes[6692] = GuestModeMessage
    _messagesTypes[9407] = ListMapNpcsQuestStatusUpdateMessage
    _messagesTypes[1501] = NpcGenericActionFailureMessage
    _messagesTypes[2360] = PortalDialogCreationMessage
    _messagesTypes[8508] = NpcDialogCreationMessage
    _messagesTypes[2122] = NpcDialogQuestionMessage
    _messagesTypes[2837] = TaxCollectorDialogQuestionBasicMessage
    _messagesTypes[9849] = TaxCollectorDialogQuestionExtendedMessage
    _messagesTypes[5982] = AllianceTaxCollectorDialogQuestionExtendedMessage
    _messagesTypes[6389] = AlliancePrismDialogQuestionMessage
    _messagesTypes[4154] = EntityTalkMessage
    _messagesTypes[8240] = JobDescriptionMessage
    _messagesTypes[3922] = JobLevelUpMessage
    _messagesTypes[7895] = JobExperienceMultiUpdateMessage
    _messagesTypes[9901] = JobExperienceUpdateMessage
    _messagesTypes[4818] = JobExperienceOtherPlayerUpdateMessage
    _messagesTypes[6676] = JobAllowMultiCraftRequestMessage
    _messagesTypes[5866] = JobMultiCraftAvailableSkillsMessage
    _messagesTypes[2905] = JobCrafterDirectoryListMessage
    _messagesTypes[7632] = JobCrafterDirectorySettingsMessage
    _messagesTypes[1188] = JobBookSubscriptionMessage
    _messagesTypes[2218] = JobCrafterDirectoryRemoveMessage
    _messagesTypes[4101] = JobCrafterDirectoryAddMessage
    _messagesTypes[1870] = JobCrafterDirectoryEntryMessage
    _messagesTypes[3977] = KamasUpdateMessage
    _messagesTypes[8096] = ObjectGroundAddedMessage
    _messagesTypes[8468] = ObjectGroundListAddedMessage
    _messagesTypes[5373] = ObjectGroundRemovedMessage
    _messagesTypes[4743] = ObjectGroundRemovedMultipleMessage
    _messagesTypes[1797] = InventoryContentMessage
    _messagesTypes[2287] = WatchInventoryContentMessage
    _messagesTypes[3367] = ShortcutBarContentMessage
    _messagesTypes[9784] = ShortcutBarAddErrorMessage
    _messagesTypes[7439] = ShortcutBarRemoveErrorMessage
    _messagesTypes[9976] = ShortcutBarSwapErrorMessage
    _messagesTypes[9492] = ShortcutBarRefreshMessage
    _messagesTypes[9231] = ShortcutBarRemovedMessage
    _messagesTypes[6652] = ShortcutBarReplacedMessage
    _messagesTypes[7983] = StorageInventoryContentMessage
    _messagesTypes[8712] = StorageKamasUpdateMessage
    _messagesTypes[6026] = StorageObjectUpdateMessage
    _messagesTypes[2141] = StorageObjectsUpdateMessage
    _messagesTypes[7049] = StorageObjectRemoveMessage
    _messagesTypes[9509] = StorageObjectsRemoveMessage
    _messagesTypes[2482] = SetUpdateMessage
    _messagesTypes[4739] = InventoryWeightMessage
    _messagesTypes[5879] = ObjectMovementMessage
    _messagesTypes[7116] = ObjectAddedMessage
    _messagesTypes[8613] = ObjectsAddedMessage
    _messagesTypes[5700] = GoldAddedMessage
    _messagesTypes[9352] = ObjectErrorMessage
    _messagesTypes[6390] = ObjectDeletedMessage
    _messagesTypes[6057] = ObjectsDeletedMessage
    _messagesTypes[7075] = ObjectQuantityMessage
    _messagesTypes[8174] = ObjectsQuantityMessage
    _messagesTypes[829] = ObjectModifiedMessage
    _messagesTypes[8091] = ObjectJobAddedMessage
    _messagesTypes[8927] = ObtainedItemMessage
    _messagesTypes[9026] = ObtainedItemWithBonusMessage
    _messagesTypes[9837] = LivingObjectMessageMessage
    _messagesTypes[7936] = SymbioticObjectErrorMessage
    _messagesTypes[6447] = SymbioticObjectAssociatedMessage
    _messagesTypes[1427] = WrapperObjectErrorMessage
    _messagesTypes[6952] = WrapperObjectAssociatedMessage
    _messagesTypes[6331] = MimicryObjectPreviewMessage
    _messagesTypes[7868] = MimicryObjectErrorMessage
    _messagesTypes[2699] = MimicryObjectAssociatedMessage
    _messagesTypes[9244] = InvalidPresetsMessage
    _messagesTypes[6378] = PresetsMessage
    _messagesTypes[5813] = ItemForPresetUpdateMessage
    _messagesTypes[8551] = PresetSavedMessage
    _messagesTypes[5087] = PresetSaveErrorMessage
    _messagesTypes[4352] = PresetDeleteResultMessage
    _messagesTypes[2423] = PresetUseResultMessage
    _messagesTypes[4515] = PresetUseResultWithMissingIdsMessage
    _messagesTypes[98] = ExchangeMoneyMovementInformationMessage
    _messagesTypes[1816] = ExchangeCraftCountModifiedMessage
    _messagesTypes[8683] = ExchangeObjectMessage
    _messagesTypes[6633] = ExchangeObjectAddedMessage
    _messagesTypes[4786] = ExchangeObjectsAddedMessage
    _messagesTypes[3935] = ExchangeObjectRemovedMessage
    _messagesTypes[7723] = ExchangeObjectsRemovedMessage
    _messagesTypes[3678] = ExchangeObjectModifiedMessage
    _messagesTypes[7924] = ExchangeObjectsModifiedMessage
    _messagesTypes[315] = ExchangeObjectPutInBagMessage
    _messagesTypes[9767] = ExchangeObjectRemovedFromBagMessage
    _messagesTypes[7251] = ExchangeObjectModifiedInBagMessage
    _messagesTypes[4572] = ExchangeKamaModifiedMessage
    _messagesTypes[3914] = ExchangePodsModifiedMessage
    _messagesTypes[4359] = ExchangeMultiCraftCrafterCanUseHisRessourcesMessage
    _messagesTypes[6930] = ExchangeRequestedMessage
    _messagesTypes[6276] = ExchangeRequestedTradeMessage
    _messagesTypes[268] = ExchangeStartedMessage
    _messagesTypes[5367] = ExchangeStartedWithPodsMessage
    _messagesTypes[4535] = ExchangeStartedWithStorageMessage
    _messagesTypes[1678] = ExchangeBidHouseBuyResultMessage
    _messagesTypes[3308] = ExchangeBidHouseItemAddOkMessage
    _messagesTypes[3056] = ExchangeBidHouseItemRemoveOkMessage
    _messagesTypes[554] = ExchangeBidHouseGenericItemAddedMessage
    _messagesTypes[9863] = ExchangeBidHouseGenericItemRemovedMessage
    _messagesTypes[7717] = ExchangeBidHouseInListAddedMessage
    _messagesTypes[5004] = ExchangeBidHouseInListUpdatedMessage
    _messagesTypes[3886] = ExchangeBidHouseInListRemovedMessage
    _messagesTypes[2886] = ExchangeBidHouseUnsoldItemsMessage
    _messagesTypes[6012] = ExchangeOfflineSoldItemsMessage
    _messagesTypes[3414] = ExchangeIsReadyMessage
    _messagesTypes[6845] = ExchangeStoppedMessage
    _messagesTypes[3014] = ExchangeErrorMessage
    _messagesTypes[5922] = ExchangeLeaveMessage
    _messagesTypes[3524] = DecraftResultMessage
    _messagesTypes[1416] = RecycleResultMessage
    _messagesTypes[2342] = ExchangeStartOkNpcTradeMessage
    _messagesTypes[927] = ExchangeStartOkRunesTradeMessage
    _messagesTypes[7078] = ExchangeStartOkEvolutiveObjectRecycleTradeMessage
    _messagesTypes[8653] = EvolutiveObjectRecycleResultMessage
    _messagesTypes[6635] = ExchangeStartOkRecycleTradeMessage
    _messagesTypes[3711] = ExchangeStartOkNpcShopMessage
    _messagesTypes[8687] = ExchangeOkMultiCraftMessage
    _messagesTypes[5921] = ExchangeCraftResultMessage
    _messagesTypes[7497] = ExchangeCraftResultWithObjectIdMessage
    _messagesTypes[1134] = ExchangeCraftResultWithObjectDescMessage
    _messagesTypes[2638] = ExchangeCraftResultMagicWithObjectDescMessage
    _messagesTypes[627] = ExchangeStartOkHumanVendorMessage
    _messagesTypes[7787] = ExchangeShopStockStartedMessage
    _messagesTypes[5416] = ExchangeShopStockMovementUpdatedMessage
    _messagesTypes[4703] = ExchangeShopStockMultiMovementUpdatedMessage
    _messagesTypes[7314] = ExchangeShopStockMovementRemovedMessage
    _messagesTypes[8793] = ExchangeShopStockMultiMovementRemovedMessage
    _messagesTypes[3642] = ExchangeStartedMountStockMessage
    _messagesTypes[1974] = ExchangeStartedTaxCollectorShopMessage
    _messagesTypes[2021] = ExchangeStartedBidSellerMessage
    _messagesTypes[9253] = ExchangeStartedBidBuyerMessage
    _messagesTypes[4385] = ExchangeBidPriceMessage
    _messagesTypes[2252] = ExchangeBidPriceForSellerMessage
    _messagesTypes[5329] = ExchangeTypesExchangerDescriptionForUserMessage
    _messagesTypes[5554] = ExchangeTypesItemsExchangerDescriptionForUserMessage
    _messagesTypes[1225] = ExchangeWeightMessage
    _messagesTypes[8831] = ExchangeGuildTaxCollectorGetMessage
    _messagesTypes[5212] = ItemNoMoreAvailableMessage
    _messagesTypes[8692] = ExchangeBuyOkMessage
    _messagesTypes[1617] = ExchangeSellOkMessage
    _messagesTypes[4036] = ExchangeReplyTaxVendorMessage
    _messagesTypes[1456] = ExchangeWaitingResultMessage
    _messagesTypes[257] = ExchangeStartOkMountWithOutPaddockMessage
    _messagesTypes[1351] = ExchangeStartOkMountMessage
    _messagesTypes[9364] = ExchangeMountStableErrorMessage
    _messagesTypes[3365] = ExchangeMountsStableAddMessage
    _messagesTypes[6928] = ExchangeMountsPaddockAddMessage
    _messagesTypes[4141] = ExchangeMountsStableBornAddMessage
    _messagesTypes[4382] = ExchangeMountsStableRemoveMessage
    _messagesTypes[4356] = ExchangeMountsPaddockRemoveMessage
    _messagesTypes[836] = ExchangeMountsTakenFromPaddockMessage
    _messagesTypes[3489] = ExchangeMountFreeFromPaddockMessage
    _messagesTypes[7786] = ExchangeMountSterilizeFromPaddockMessage
    _messagesTypes[7437] = ExchangeBidSearchOkMessage
    _messagesTypes[321] = ExchangeItemAutoCraftStopedMessage
    _messagesTypes[4876] = ExchangeStartOkCraftMessage
    _messagesTypes[1180] = ExchangeStartOkCraftWithInformationMessage
    _messagesTypes[7885] = ExchangeStartOkMulticraftCrafterMessage
    _messagesTypes[3366] = ExchangeStartOkMulticraftCustomerMessage
    _messagesTypes[7102] = ExchangeCrafterJobLevelupMessage
    _messagesTypes[7830] = ExchangeStartOkJobIndexMessage
    _messagesTypes[9955] = ExchangeCraftPaymentModifiedMessage
    _messagesTypes[4691] = UpdateMountCharacteristicsMessage
    _messagesTypes[6484] = ObjectAveragePricesErrorMessage
    _messagesTypes[2074] = ObjectAveragePricesMessage
    _messagesTypes[9506] = PurchasableDialogMessage
    _messagesTypes[6940] = AccountHouseMessage
    _messagesTypes[1755] = HousePropertiesMessage
    _messagesTypes[5020] = HouseBuyResultMessage
    _messagesTypes[9319] = HouseSellingUpdateMessage
    _messagesTypes[824] = HouseToSellListMessage
    _messagesTypes[5178] = HouseGuildNoneMessage
    _messagesTypes[6131] = HouseGuildRightsMessage
    _messagesTypes[3573] = PaddockBuyResultMessage
    _messagesTypes[3099] = PaddockPropertiesMessage
    _messagesTypes[375] = PaddockSellBuyDialogMessage
    _messagesTypes[1970] = GameDataPlayFarmObjectAnimationMessage
    _messagesTypes[7367] = PaddockToSellListMessage
    _messagesTypes[5991] = HavenBagRoomUpdateMessage
    _messagesTypes[8638] = HavenBagPackListMessage
    _messagesTypes[6843] = EditHavenBagStartMessage
    _messagesTypes[7671] = EditHavenBagFinishedMessage
    _messagesTypes[2601] = HavenBagDailyLoteryMessage
    _messagesTypes[8483] = HavenBagFurnituresMessage
    _messagesTypes[2912] = MapComplementaryInformationsDataInHavenBagMessage
    _messagesTypes[6792] = HavenBagPermissionsUpdateMessage
    _messagesTypes[5668] = InviteInHavenBagClosedMessage
    _messagesTypes[8351] = InviteInHavenBagMessage
    _messagesTypes[7339] = InviteInHavenBagOfferMessage
    _messagesTypes[9116] = MountSterilizedMessage
    _messagesTypes[3662] = MountReleasedMessage
    _messagesTypes[2241] = MountRenamedMessage
    _messagesTypes[6028] = MountXpRatioMessage
    _messagesTypes[391] = MountDataMessage
    _messagesTypes[1524] = MountDataErrorMessage
    _messagesTypes[4558] = MountSetMessage
    _messagesTypes[8851] = MountUnSetMessage
    _messagesTypes[9383] = MountEquipedErrorMessage
    _messagesTypes[8146] = MountRidingMessage
    _messagesTypes[2442] = GameDataPaddockObjectRemoveMessage
    _messagesTypes[2165] = GameDataPaddockObjectAddMessage
    _messagesTypes[11] = GameDataPaddockObjectListAddMessage
    _messagesTypes[6579] = MountEmoteIconUsedOkMessage
    _messagesTypes[5125] = LockableShowCodeDialogMessage
    _messagesTypes[6569] = LockableCodeResultMessage
    _messagesTypes[8803] = LockableStateUpdateAbstractMessage
    _messagesTypes[990] = LockableStateUpdateHouseDoorMessage
    _messagesTypes[9912] = LockableStateUpdateStorageMessage
    _messagesTypes[2676] = DocumentReadingBeginMessage
    _messagesTypes[3990] = TitlesAndOrnamentsListMessage
    _messagesTypes[5524] = TitleGainedMessage
    _messagesTypes[6491] = TitleLostMessage
    _messagesTypes[8779] = OrnamentGainedMessage
    _messagesTypes[1592] = OrnamentLostMessage
    _messagesTypes[1578] = TitleSelectedMessage
    _messagesTypes[6658] = TitleSelectErrorMessage
    _messagesTypes[7210] = OrnamentSelectedMessage
    _messagesTypes[4197] = OrnamentSelectErrorMessage
    _messagesTypes[2975] = ContactLookMessage
    _messagesTypes[8688] = ContactLookErrorMessage
    _messagesTypes[7363] = SocialNoticeMessage
    _messagesTypes[5239] = BulletinMessage
    _messagesTypes[1573] = SocialNoticeSetErrorMessage
    _messagesTypes[6646] = AccessoryPreviewErrorMessage
    _messagesTypes[5662] = AccessoryPreviewMessage
    _messagesTypes[5285] = HaapiBufferListMessage
    _messagesTypes[7202] = HaapiConfirmationMessage
    _messagesTypes[1415] = HaapiValidationMessage
    _messagesTypes[1897] = HaapiBuyValidationMessage
    _messagesTypes[30] = HaapiApiKeyMessage
    _messagesTypes[6657] = HaapiShopApiKeyMessage
    _messagesTypes[820] = FinishMoveListMessage
    _messagesTypes[9173] = TreasureHuntShowLegendaryUIMessage
    _messagesTypes[6318] = TreasureHuntRequestAnswerMessage
    _messagesTypes[7652] = TreasureHuntMessage
    _messagesTypes[4798] = TreasureHuntFinishedMessage
    _messagesTypes[6919] = TreasureHuntDigRequestAnswerMessage
    _messagesTypes[3869] = TreasureHuntDigRequestAnswerFailedMessage
    _messagesTypes[309] = TreasureHuntFlagRequestAnswerMessage
    _messagesTypes[5909] = TreasureHuntAvailableRetryCountUpdateMessage
    _messagesTypes[6075] = BreachStateMessage
    _messagesTypes[253] = BreachCharactersMessage
    _messagesTypes[1240] = BreachBonusMessage
    _messagesTypes[8787] = BreachBudgetMessage
    _messagesTypes[593] = BreachSavedMessage
    _messagesTypes[2636] = BreachBranchesMessage
    _messagesTypes[6368] = BreachRewardsMessage
    _messagesTypes[8594] = BreachRewardBoughtMessage
    _messagesTypes[423] = BreachInvitationOfferMessage
    _messagesTypes[995] = BreachInvitationResponseMessage
    _messagesTypes[5791] = BreachInvitationCloseMessage
    _messagesTypes[6036] = BreachKickResponseMessage
    _messagesTypes[8497] = AnomalySubareaInformationResponseMessage
    _messagesTypes[4206] = AlignmentWarEffortProgressionMessage
    _messagesTypes[3065] = CharacterAlignmentWarEffortProgressionMessage
    _messagesTypes[9897] = AlignmentWarEffortDonatePreviewMessage
    _messagesTypes[9607] = AlignmentWarEffortDonationResultMessage
    _messagesTypes[876] = HaapiTokenMessage
    _messagesTypes[7425] = HaapiAuthErrorMessage
    _messagesTypes[1564] = HaapiSessionMessage
    _messagesTypes[7615] = DebtsUpdateMessage
    _messagesTypes[9246] = DebtsDeleteMessage
    _messagesTypes[8161] = ActivitySuggestionsMessage
    _unpackModes[9279] = UnpackMode.ASYNC

    def __init__(self):
        super().__init__()

    def register(self) -> None:
        StoreDataManager().registerClass(PaginationAnswerAbstractMessage(), True, True)
        StoreDataManager().registerClass(NetworkDataContainerMessage(), True, True)
        StoreDataManager().registerClass(ProtocolRequired(), True, True)
        StoreDataManager().registerClass(LoginQueueStatusMessage(), True, True)
        StoreDataManager().registerClass(QueueStatusMessage(), True, True)
        StoreDataManager().registerClass(ConsoleMessage(), True, True)
        StoreDataManager().registerClass(ConsoleCommandsListMessage(), True, True)
        StoreDataManager().registerClass(HelloConnectMessage(), True, True)
        StoreDataManager().registerClass(
            CredentialsAcknowledgementMessage(), True, True
        )
        StoreDataManager().registerClass(NicknameRegistrationMessage(), True, True)
        StoreDataManager().registerClass(AccountLinkRequiredMessage(), True, True)
        StoreDataManager().registerClass(NicknameRefusedMessage(), True, True)
        StoreDataManager().registerClass(NicknameAcceptedMessage(), True, True)
        StoreDataManager().registerClass(IdentificationSuccessMessage(), True, True)
        StoreDataManager().registerClass(
            IdentificationSuccessWithLoginTokenMessage(), True, True
        )
        StoreDataManager().registerClass(IdentificationFailedMessage(), True, True)
        StoreDataManager().registerClass(
            IdentificationFailedBannedMessage(), True, True
        )
        StoreDataManager().registerClass(
            IdentificationFailedForBadVersionMessage(), True, True
        )
        StoreDataManager().registerClass(ServersListMessage(), True, True)
        StoreDataManager().registerClass(ServerStatusUpdateMessage(), True, True)
        StoreDataManager().registerClass(SelectedServerDataMessage(), True, True)
        StoreDataManager().registerClass(
            SelectedServerDataExtendedMessage(), True, True
        )
        StoreDataManager().registerClass(SelectedServerRefusedMessage(), True, True)
        StoreDataManager().registerClass(AcquaintanceSearchErrorMessage(), True, True)
        StoreDataManager().registerClass(AcquaintanceServerListMessage(), True, True)
        StoreDataManager().registerClass(MigratedServerListMessage(), True, True)
        StoreDataManager().registerClass(HelloGameMessage(), True, True)
        StoreDataManager().registerClass(
            AuthenticationTicketAcceptedMessage(), True, True
        )
        StoreDataManager().registerClass(
            AuthenticationTicketRefusedMessage(), True, True
        )
        StoreDataManager().registerClass(AlreadyConnectedMessage(), True, True)
        StoreDataManager().registerClass(AccountLoggingKickedMessage(), True, True)
        StoreDataManager().registerClass(ReloginTokenStatusMessage(), True, True)
        StoreDataManager().registerClass(ServerSettingsMessage(), True, True)
        StoreDataManager().registerClass(ServerSessionConstantsMessage(), True, True)
        StoreDataManager().registerClass(ServerOptionalFeaturesMessage(), True, True)
        StoreDataManager().registerClass(AccountCapabilitiesMessage(), True, True)
        StoreDataManager().registerClass(TrustStatusMessage(), True, True)
        StoreDataManager().registerClass(AccountInformationsUpdateMessage(), True, True)
        StoreDataManager().registerClass(CheckFileRequestMessage(), True, True)
        StoreDataManager().registerClass(RawDataMessage(), True, True)
        StoreDataManager().registerClass(StartupActionsListMessage(), True, True)
        StoreDataManager().registerClass(StartupActionAddMessage(), True, True)
        StoreDataManager().registerClass(StartupActionFinishedMessage(), True, True)
        StoreDataManager().registerClass(
            CharacterCanBeCreatedResultMessage(), True, True
        )
        StoreDataManager().registerClass(CharacterCreationResultMessage(), True, True)
        StoreDataManager().registerClass(CharacterDeletionErrorMessage(), True, True)
        StoreDataManager().registerClass(
            CharacterNameSuggestionSuccessMessage(), True, True
        )
        StoreDataManager().registerClass(
            CharacterNameSuggestionFailureMessage(), True, True
        )
        StoreDataManager().registerClass(BasicCharactersListMessage(), True, True)
        StoreDataManager().registerClass(CharactersListMessage(), True, True)
        StoreDataManager().registerClass(
            CharactersListWithRemodelingMessage(), True, True
        )
        StoreDataManager().registerClass(CharactersListErrorMessage(), True, True)
        StoreDataManager().registerClass(CharacterSelectedSuccessMessage(), True, True)
        StoreDataManager().registerClass(CharacterSelectedForceMessage(), True, True)
        StoreDataManager().registerClass(CharacterSelectedErrorMessage(), True, True)
        StoreDataManager().registerClass(PopupWarningMessage(), True, True)
        StoreDataManager().registerClass(PopupWarningClosedMessage(), True, True)
        StoreDataManager().registerClass(BasicDateMessage(), True, True)
        StoreDataManager().registerClass(BasicTimeMessage(), True, True)
        StoreDataManager().registerClass(AlmanachCalendarDateMessage(), True, True)
        StoreDataManager().registerClass(BasicNoOperationMessage(), True, True)
        StoreDataManager().registerClass(BasicAckMessage(), True, True)
        StoreDataManager().registerClass(SystemMessageDisplayMessage(), True, True)
        StoreDataManager().registerClass(TextInformationMessage(), True, True)
        StoreDataManager().registerClass(OnConnectionEventMessage(), True, True)
        StoreDataManager().registerClass(SetCharacterRestrictionsMessage(), True, True)
        StoreDataManager().registerClass(
            ServerExperienceModificatorMessage(), True, True
        )
        StoreDataManager().registerClass(CharacterCapabilitiesMessage(), True, True)
        StoreDataManager().registerClass(CharacterLoadingCompleteMessage(), True, True)
        StoreDataManager().registerClass(GameContextCreateMessage(), True, True)
        StoreDataManager().registerClass(GameContextCreateErrorMessage(), True, True)
        StoreDataManager().registerClass(GameContextDestroyMessage(), True, True)
        StoreDataManager().registerClass(GameContextRemoveElementMessage(), True, True)
        StoreDataManager().registerClass(
            GameContextRemoveMultipleElementsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameContextRemoveElementWithEventMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameContextRemoveMultipleElementsWithEventsMessage(), True, True
        )
        StoreDataManager().registerClass(GameContextMoveElementMessage(), True, True)
        StoreDataManager().registerClass(
            GameContextMoveMultipleElementsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameContextRefreshEntityLookMessage(), True, True
        )
        StoreDataManager().registerClass(GameMapSpeedMovementMessage(), True, True)
        StoreDataManager().registerClass(GameMapNoMovementMessage(), True, True)
        StoreDataManager().registerClass(GameMapMovementMessage(), True, True)
        StoreDataManager().registerClass(GameCautiousMapMovementMessage(), True, True)
        StoreDataManager().registerClass(GameMapChangeOrientationMessage(), True, True)
        StoreDataManager().registerClass(GameMapChangeOrientationsMessage(), True, True)
        StoreDataManager().registerClass(GameEntityDispositionMessage(), True, True)
        StoreDataManager().registerClass(GameEntitiesDispositionMessage(), True, True)
        StoreDataManager().registerClass(
            GameEntityDispositionErrorMessage(), True, True
        )
        StoreDataManager().registerClass(GameRefreshMonsterBoostsMessage(), True, True)
        StoreDataManager().registerClass(PlayerStatusUpdateErrorMessage(), True, True)
        StoreDataManager().registerClass(PlayerStatusUpdateMessage(), True, True)
        StoreDataManager().registerClass(BasicWhoIsMessage(), True, True)
        StoreDataManager().registerClass(BasicWhoIsNoMatchMessage(), True, True)
        StoreDataManager().registerClass(NumericWhoIsMessage(), True, True)
        StoreDataManager().registerClass(BasicPongMessage(), True, True)
        StoreDataManager().registerClass(BasicLatencyStatsRequestMessage(), True, True)
        StoreDataManager().registerClass(SequenceNumberRequestMessage(), True, True)
        StoreDataManager().registerClass(CurrentServerStatusUpdateMessage(), True, True)
        StoreDataManager().registerClass(CinematicMessage(), True, True)
        StoreDataManager().registerClass(DumpedEntityStatsMessage(), True, True)
        StoreDataManager().registerClass(DebugHighlightCellsMessage(), True, True)
        StoreDataManager().registerClass(DebugClearHighlightCellsMessage(), True, True)
        StoreDataManager().registerClass(DebugInClientMessage(), True, True)
        StoreDataManager().registerClass(ClientYouAreDrunkMessage(), True, True)
        StoreDataManager().registerClass(
            DisplayNumericalValuePaddockMessage(), True, True
        )
        StoreDataManager().registerClass(CurrentMapMessage(), True, True)
        StoreDataManager().registerClass(CurrentMapInstanceMessage(), True, True)
        StoreDataManager().registerClass(TeleportOnSameMapMessage(), True, True)
        StoreDataManager().registerClass(MapFightCountMessage(), True, True)
        StoreDataManager().registerClass(MapRunningFightListMessage(), True, True)
        StoreDataManager().registerClass(MapRunningFightDetailsMessage(), True, True)
        StoreDataManager().registerClass(
            MapRunningFightDetailsExtendedMessage(), True, True
        )
        StoreDataManager().registerClass(MapObstacleUpdateMessage(), True, True)
        StoreDataManager().registerClass(
            MapComplementaryInformationsDataMessage(), True, True
        )
        StoreDataManager().registerClass(
            MapComplementaryInformationsDataInHouseMessage(), True, True
        )
        StoreDataManager().registerClass(
            MapComplementaryInformationsWithCoordsMessage(), True, True
        )
        StoreDataManager().registerClass(MapRewardRateMessage(), True, True)
        StoreDataManager().registerClass(BreachEnterMessage(), True, True)
        StoreDataManager().registerClass(BreachTeleportResponseMessage(), True, True)
        StoreDataManager().registerClass(BreachRoomLockedMessage(), True, True)
        StoreDataManager().registerClass(BreachRoomUnlockResultMessage(), True, True)
        StoreDataManager().registerClass(BreachExitResponseMessage(), True, True)
        StoreDataManager().registerClass(
            MapComplementaryInformationsBreachMessage(), True, True
        )
        StoreDataManager().registerClass(BreachGameFightEndMessage(), True, True)
        StoreDataManager().registerClass(AnomalyStateMessage(), True, True)
        StoreDataManager().registerClass(
            MapComplementaryInformationsAnomalyMessage(), True, True
        )
        StoreDataManager().registerClass(
            MapFightStartPositionsUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(GameRolePlayShowActorMessage(), True, True)
        StoreDataManager().registerClass(
            GameRolePlayShowMultipleActorsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayShowActorWithEventMessage(), True, True
        )
        StoreDataManager().registerClass(CharacterStatsListMessage(), True, True)
        StoreDataManager().registerClass(FighterStatsListMessage(), True, True)
        StoreDataManager().registerClass(UpdateSpellModifierMessage(), True, True)
        StoreDataManager().registerClass(CharacterLevelUpMessage(), True, True)
        StoreDataManager().registerClass(CharacterExperienceGainMessage(), True, True)
        StoreDataManager().registerClass(
            CharacterLevelUpInformationMessage(), True, True
        )
        StoreDataManager().registerClass(UpdateLifePointsMessage(), True, True)
        StoreDataManager().registerClass(LifePointsRegenBeginMessage(), True, True)
        StoreDataManager().registerClass(LifePointsRegenEndMessage(), True, True)
        StoreDataManager().registerClass(
            GameRolePlayPlayerLifeStatusMessage(), True, True
        )
        StoreDataManager().registerClass(GameRolePlayGameOverMessage(), True, True)
        StoreDataManager().registerClass(
            GameRolePlayFightRequestCanceledMessage(), True, True
        )
        StoreDataManager().registerClass(GameRolePlayAggressionMessage(), True, True)
        StoreDataManager().registerClass(
            GameRolePlayPlayerFightFriendlyRequestedMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayPlayerFightFriendlyAnsweredMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaRegistrationStatusMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaFightPropositionMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaFighterStatusMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaUpdatePlayerInfosMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaSwitchToFightServerMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaSwitchToGameServerMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaInvitationCandidatesAnswerMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaLeagueRewardsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaPlayerBehavioursMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayArenaRegistrationWarningMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayMonsterAngryAtPlayerMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayMonsterNotAngryAtPlayerMessage(), True, True
        )
        StoreDataManager().registerClass(GameRolePlayShowChallengeMessage(), True, True)
        StoreDataManager().registerClass(
            GameRolePlayRemoveChallengeMessage(), True, True
        )
        StoreDataManager().registerClass(GameRolePlaySpellAnimMessage(), True, True)
        StoreDataManager().registerClass(GameRolePlayDelayedActionMessage(), True, True)
        StoreDataManager().registerClass(
            GameRolePlayDelayedObjectUseMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameRolePlayDelayedActionFinishedMessage(), True, True
        )
        StoreDataManager().registerClass(ShowCellMessage(), True, True)
        StoreDataManager().registerClass(ShowCellSpectatorMessage(), True, True)
        StoreDataManager().registerClass(GameFightStartingMessage(), True, True)
        StoreDataManager().registerClass(GameFightJoinMessage(), True, True)
        StoreDataManager().registerClass(GameFightSpectatorJoinMessage(), True, True)
        StoreDataManager().registerClass(
            GameFightPlacementPossiblePositionsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameFightPlacementSwapPositionsErrorMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameFightPlacementSwapPositionsOfferMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameFightPlacementSwapPositionsCancelledMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameFightPlacementSwapPositionsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameFightOptionStateUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(GameFightUpdateTeamMessage(), True, True)
        StoreDataManager().registerClass(GameFightRemoveTeamMemberMessage(), True, True)
        StoreDataManager().registerClass(GameFightHumanReadyStateMessage(), True, True)
        StoreDataManager().registerClass(GameFightLeaveMessage(), True, True)
        StoreDataManager().registerClass(GameFightStartMessage(), True, True)
        StoreDataManager().registerClass(GameFightSpectateMessage(), True, True)
        StoreDataManager().registerClass(GameFightResumeMessage(), True, True)
        StoreDataManager().registerClass(GameFightResumeWithSlavesMessage(), True, True)
        StoreDataManager().registerClass(GameFightEndMessage(), True, True)
        StoreDataManager().registerClass(GameFightNewRoundMessage(), True, True)
        StoreDataManager().registerClass(GameFightTurnListMessage(), True, True)
        StoreDataManager().registerClass(GameFightTurnStartMessage(), True, True)
        StoreDataManager().registerClass(GameFightNewWaveMessage(), True, True)
        StoreDataManager().registerClass(GameFightTurnStartPlayingMessage(), True, True)
        StoreDataManager().registerClass(GameFightTurnResumeMessage(), True, True)
        StoreDataManager().registerClass(GameFightPauseMessage(), True, True)
        StoreDataManager().registerClass(SlaveSwitchContextMessage(), True, True)
        StoreDataManager().registerClass(SlaveNoLongerControledMessage(), True, True)
        StoreDataManager().registerClass(RefreshCharacterStatsMessage(), True, True)
        StoreDataManager().registerClass(GameFightTurnReadyRequestMessage(), True, True)
        StoreDataManager().registerClass(GameFightSynchronizeMessage(), True, True)
        StoreDataManager().registerClass(GameFightTurnEndMessage(), True, True)
        StoreDataManager().registerClass(GameFightShowFighterMessage(), True, True)
        StoreDataManager().registerClass(GameFightRefreshFighterMessage(), True, True)
        StoreDataManager().registerClass(
            GameFightShowFighterRandomStaticPoseMessage(), True, True
        )
        StoreDataManager().registerClass(ArenaFighterLeaveMessage(), True, True)
        StoreDataManager().registerClass(ArenaFighterIdleMessage(), True, True)
        StoreDataManager().registerClass(SequenceStartMessage(), True, True)
        StoreDataManager().registerClass(SequenceEndMessage(), True, True)
        StoreDataManager().registerClass(AbstractGameActionMessage(), True, True)
        StoreDataManager().registerClass(GameActionNoopMessage(), True, True)
        StoreDataManager().registerClass(GameActionSpamMessage(), True, True)
        StoreDataManager().registerClass(AbstractGameActionWithAckMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightNoSpellCastMessage(), True, True
        )
        StoreDataManager().registerClass(
            AbstractGameActionFightTargetedAbilityMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightSpellCastMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightCloseCombatMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionUpdateEffectTriggerCountMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightInvisibleDetectedMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightPointsVariationMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightTackledMessage(), True, True)
        StoreDataManager().registerClass(GameActionFightDeathMessage(), True, True)
        StoreDataManager().registerClass(GameActionFightKillMessage(), True, True)
        StoreDataManager().registerClass(GameActionFightVanishMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightSpellCooldownVariationMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightSpellImmunityMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightLifePointsGainMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightLifePointsLostMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightLifeAndShieldPointsLostMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightDispellableEffectMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightReflectSpellMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightReduceDamagesMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightReflectDamagesMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightDodgePointLossMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightSlideMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightTeleportOnSameMapMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightExchangePositionsMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightDispellMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightDispellEffectMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightDispellSpellMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightModifyEffectsDurationMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightTriggerEffectMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightStealKamaMessage(), True, True)
        StoreDataManager().registerClass(GameActionFightChangeLookMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightInvisibilityMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightSummonMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightMultipleSummonMessage(), True, True
        )
        StoreDataManager().registerClass(GameActionFightMarkCellsMessage(), True, True)
        StoreDataManager().registerClass(
            GameActionFightUnmarkCellsMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightTriggerGlyphTrapMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightActivateGlyphTrapMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightCarryCharacterMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightThrowCharacterMessage(), True, True
        )
        StoreDataManager().registerClass(
            GameActionFightDropCharacterMessage(), True, True
        )
        StoreDataManager().registerClass(EmoteListMessage(), True, True)
        StoreDataManager().registerClass(EmoteAddMessage(), True, True)
        StoreDataManager().registerClass(EmoteRemoveMessage(), True, True)
        StoreDataManager().registerClass(EmotePlayAbstractMessage(), True, True)
        StoreDataManager().registerClass(EmotePlayMessage(), True, True)
        StoreDataManager().registerClass(EmotePlayMassiveMessage(), True, True)
        StoreDataManager().registerClass(EmotePlayErrorMessage(), True, True)
        StoreDataManager().registerClass(ChatSmileyMessage(), True, True)
        StoreDataManager().registerClass(
            ChatCommunityChannelCommunityMessage(), True, True
        )
        StoreDataManager().registerClass(LocalizedChatSmileyMessage(), True, True)
        StoreDataManager().registerClass(MoodSmileyResultMessage(), True, True)
        StoreDataManager().registerClass(MoodSmileyUpdateMessage(), True, True)
        StoreDataManager().registerClass(ChatSmileyExtraPackListMessage(), True, True)
        StoreDataManager().registerClass(ChatAbstractServerMessage(), True, True)
        StoreDataManager().registerClass(ChatServerMessage(), True, True)
        StoreDataManager().registerClass(ChatKolizeumServerMessage(), True, True)
        StoreDataManager().registerClass(ChatAdminServerMessage(), True, True)
        StoreDataManager().registerClass(ChatServerWithObjectMessage(), True, True)
        StoreDataManager().registerClass(ChatServerCopyMessage(), True, True)
        StoreDataManager().registerClass(ChatServerCopyWithObjectMessage(), True, True)
        StoreDataManager().registerClass(ChatErrorMessage(), True, True)
        StoreDataManager().registerClass(EnabledChannelsMessage(), True, True)
        StoreDataManager().registerClass(ChannelEnablingChangeMessage(), True, True)
        StoreDataManager().registerClass(SpellListMessage(), True, True)
        StoreDataManager().registerClass(
            ForgettableSpellListUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(ForgettableSpellDeleteMessage(), True, True)
        StoreDataManager().registerClass(
            ForgettableSpellEquipmentSlotsMessage(), True, True
        )
        StoreDataManager().registerClass(LeaveDialogMessage(), True, True)
        StoreDataManager().registerClass(PauseDialogMessage(), True, True)
        StoreDataManager().registerClass(InteractiveUseErrorMessage(), True, True)
        StoreDataManager().registerClass(InteractiveUsedMessage(), True, True)
        StoreDataManager().registerClass(InteractiveUseEndedMessage(), True, True)
        StoreDataManager().registerClass(InteractiveMapUpdateMessage(), True, True)
        StoreDataManager().registerClass(StatedMapUpdateMessage(), True, True)
        StoreDataManager().registerClass(InteractiveElementUpdatedMessage(), True, True)
        StoreDataManager().registerClass(StatedElementUpdatedMessage(), True, True)
        StoreDataManager().registerClass(ZaapRespawnUpdatedMessage(), True, True)
        StoreDataManager().registerClass(TeleportDestinationsMessage(), True, True)
        StoreDataManager().registerClass(ZaapDestinationsMessage(), True, True)
        StoreDataManager().registerClass(KnownZaapListMessage(), True, True)
        StoreDataManager().registerClass(TeleportBuddiesMessage(), True, True)
        StoreDataManager().registerClass(TeleportBuddiesRequestedMessage(), True, True)
        StoreDataManager().registerClass(TeleportToBuddyOfferMessage(), True, True)
        StoreDataManager().registerClass(TeleportToBuddyCloseMessage(), True, True)
        StoreDataManager().registerClass(SpellVariantActivationMessage(), True, True)
        StoreDataManager().registerClass(StatsUpgradeResultMessage(), True, True)
        StoreDataManager().registerClass(ChallengeTargetsListMessage(), True, True)
        StoreDataManager().registerClass(ChallengeInfoMessage(), True, True)
        StoreDataManager().registerClass(ChallengeTargetUpdateMessage(), True, True)
        StoreDataManager().registerClass(ChallengeResultMessage(), True, True)
        StoreDataManager().registerClass(EntityInformationMessage(), True, True)
        StoreDataManager().registerClass(EntitiesInformationMessage(), True, True)
        StoreDataManager().registerClass(IdolSelectErrorMessage(), True, True)
        StoreDataManager().registerClass(IdolSelectedMessage(), True, True)
        StoreDataManager().registerClass(IdolListMessage(), True, True)
        StoreDataManager().registerClass(IdolPartyRefreshMessage(), True, True)
        StoreDataManager().registerClass(IdolPartyLostMessage(), True, True)
        StoreDataManager().registerClass(
            IdolFightPreparationUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(AchievementListMessage(), True, True)
        StoreDataManager().registerClass(AchievementDetailsMessage(), True, True)
        StoreDataManager().registerClass(AchievementDetailedListMessage(), True, True)
        StoreDataManager().registerClass(
            AchievementAlmostFinishedDetailedListMessage(), True, True
        )
        StoreDataManager().registerClass(AchievementFinishedMessage(), True, True)
        StoreDataManager().registerClass(
            AchievementFinishedInformationMessage(), True, True
        )
        StoreDataManager().registerClass(AchievementRewardSuccessMessage(), True, True)
        StoreDataManager().registerClass(AchievementRewardErrorMessage(), True, True)
        StoreDataManager().registerClass(
            FriendGuildWarnOnAchievementCompleteStateMessage(), True, True
        )
        StoreDataManager().registerClass(DungeonKeyRingMessage(), True, True)
        StoreDataManager().registerClass(DungeonKeyRingUpdateMessage(), True, True)
        StoreDataManager().registerClass(
            UpdateMapPlayersAgressableStatusMessage(), True, True
        )
        StoreDataManager().registerClass(
            UpdateSelfAgressableStatusMessage(), True, True
        )
        StoreDataManager().registerClass(AlignmentRankUpdateMessage(), True, True)
        StoreDataManager().registerClass(CompassResetMessage(), True, True)
        StoreDataManager().registerClass(CompassUpdateMessage(), True, True)
        StoreDataManager().registerClass(CompassUpdatePartyMemberMessage(), True, True)
        StoreDataManager().registerClass(AtlasPointInformationsMessage(), True, True)
        StoreDataManager().registerClass(CompassUpdatePvpSeekMessage(), True, True)
        StoreDataManager().registerClass(AbstractPartyMessage(), True, True)
        StoreDataManager().registerClass(AbstractPartyEventMessage(), True, True)
        StoreDataManager().registerClass(PartyModifiableStatusMessage(), True, True)
        StoreDataManager().registerClass(PartyInvitationMessage(), True, True)
        StoreDataManager().registerClass(PartyInvitationDungeonMessage(), True, True)
        StoreDataManager().registerClass(PartyInvitationDetailsMessage(), True, True)
        StoreDataManager().registerClass(
            PartyInvitationDungeonDetailsMessage(), True, True
        )
        StoreDataManager().registerClass(
            PartyInvitationCancelledForGuestMessage(), True, True
        )
        StoreDataManager().registerClass(
            PartyCancelInvitationNotificationMessage(), True, True
        )
        StoreDataManager().registerClass(
            PartyRefuseInvitationNotificationMessage(), True, True
        )
        StoreDataManager().registerClass(PartyCannotJoinErrorMessage(), True, True)
        StoreDataManager().registerClass(PartyJoinMessage(), True, True)
        StoreDataManager().registerClass(PartyNewGuestMessage(), True, True)
        StoreDataManager().registerClass(PartyUpdateMessage(), True, True)
        StoreDataManager().registerClass(PartyNewMemberMessage(), True, True)
        StoreDataManager().registerClass(PartyUpdateLightMessage(), True, True)
        StoreDataManager().registerClass(PartyEntityUpdateLightMessage(), True, True)
        StoreDataManager().registerClass(PartyMemberRemoveMessage(), True, True)
        StoreDataManager().registerClass(PartyMemberEjectedMessage(), True, True)
        StoreDataManager().registerClass(PartyLeaderUpdateMessage(), True, True)
        StoreDataManager().registerClass(PartyFollowStatusUpdateMessage(), True, True)
        StoreDataManager().registerClass(PartyLocateMembersMessage(), True, True)
        StoreDataManager().registerClass(PartyLeaveMessage(), True, True)
        StoreDataManager().registerClass(PartyKickedByMessage(), True, True)
        StoreDataManager().registerClass(PartyRestrictedMessage(), True, True)
        StoreDataManager().registerClass(PartyDeletedMessage(), True, True)
        StoreDataManager().registerClass(PartyLoyaltyStatusMessage(), True, True)
        StoreDataManager().registerClass(
            AbstractPartyMemberInFightMessage(), True, True
        )
        StoreDataManager().registerClass(
            PartyMemberInStandardFightMessage(), True, True
        )
        StoreDataManager().registerClass(PartyMemberInBreachFightMessage(), True, True)
        StoreDataManager().registerClass(PartyNameUpdateMessage(), True, True)
        StoreDataManager().registerClass(PartyNameSetErrorMessage(), True, True)
        StoreDataManager().registerClass(
            DungeonPartyFinderAvailableDungeonsMessage(), True, True
        )
        StoreDataManager().registerClass(
            DungeonPartyFinderListenErrorMessage(), True, True
        )
        StoreDataManager().registerClass(
            DungeonPartyFinderRoomContentMessage(), True, True
        )
        StoreDataManager().registerClass(
            DungeonPartyFinderRoomContentUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(
            DungeonPartyFinderRegisterSuccessMessage(), True, True
        )
        StoreDataManager().registerClass(
            DungeonPartyFinderRegisterErrorMessage(), True, True
        )
        StoreDataManager().registerClass(ContactAddFailureMessage(), True, True)
        StoreDataManager().registerClass(SpouseStatusMessage(), True, True)
        StoreDataManager().registerClass(FriendsListMessage(), True, True)
        StoreDataManager().registerClass(AcquaintancesListMessage(), True, True)
        StoreDataManager().registerClass(SpouseInformationsMessage(), True, True)
        StoreDataManager().registerClass(FriendAddFailureMessage(), True, True)
        StoreDataManager().registerClass(AcquaintanceAddedMessage(), True, True)
        StoreDataManager().registerClass(FriendAddedMessage(), True, True)
        StoreDataManager().registerClass(FriendUpdateMessage(), True, True)
        StoreDataManager().registerClass(FriendDeleteResultMessage(), True, True)
        StoreDataManager().registerClass(
            FriendWarnOnConnectionStateMessage(), True, True
        )
        StoreDataManager().registerClass(WarnOnPermaDeathStateMessage(), True, True)
        StoreDataManager().registerClass(
            FriendWarnOnLevelGainStateMessage(), True, True
        )
        StoreDataManager().registerClass(FriendStatusShareStateMessage(), True, True)
        StoreDataManager().registerClass(IgnoredListMessage(), True, True)
        StoreDataManager().registerClass(IgnoredAddFailureMessage(), True, True)
        StoreDataManager().registerClass(IgnoredAddedMessage(), True, True)
        StoreDataManager().registerClass(IgnoredDeleteResultMessage(), True, True)
        StoreDataManager().registerClass(AllianceCreationStartedMessage(), True, True)
        StoreDataManager().registerClass(
            AllianceModificationStartedMessage(), True, True
        )
        StoreDataManager().registerClass(AllianceCreationResultMessage(), True, True)
        StoreDataManager().registerClass(AllianceInvitedMessage(), True, True)
        StoreDataManager().registerClass(
            AllianceInvitationStateRecruterMessage(), True, True
        )
        StoreDataManager().registerClass(
            AllianceInvitationStateRecrutedMessage(), True, True
        )
        StoreDataManager().registerClass(AllianceJoinedMessage(), True, True)
        StoreDataManager().registerClass(AllianceGuildLeavingMessage(), True, True)
        StoreDataManager().registerClass(AllianceLeftMessage(), True, True)
        StoreDataManager().registerClass(AllianceMembershipMessage(), True, True)
        StoreDataManager().registerClass(AllianceSummaryMessage(), True, True)
        StoreDataManager().registerClass(KohUpdateMessage(), True, True)
        StoreDataManager().registerClass(
            AreaFightModificatorUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(ClientUIOpenedMessage(), True, True)
        StoreDataManager().registerClass(ClientUIOpenedByObjectMessage(), True, True)
        StoreDataManager().registerClass(GuildLogbookInformationMessage(), True, True)
        StoreDataManager().registerClass(GuildSummaryMessage(), True, True)
        StoreDataManager().registerClass(GuildCreationStartedMessage(), True, True)
        StoreDataManager().registerClass(GuildModificationStartedMessage(), True, True)
        StoreDataManager().registerClass(GuildCreationResultMessage(), True, True)
        StoreDataManager().registerClass(GuildInvitedMessage(), True, True)
        StoreDataManager().registerClass(
            GuildInvitationStateRecruterMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildInvitationStateRecrutedMessage(), True, True
        )
        StoreDataManager().registerClass(GuildJoinedMessage(), True, True)
        StoreDataManager().registerClass(GuildMemberOnlineStatusMessage(), True, True)
        StoreDataManager().registerClass(GuildInformationsGeneralMessage(), True, True)
        StoreDataManager().registerClass(GuildInformationsMembersMessage(), True, True)
        StoreDataManager().registerClass(
            GuildInformationsMemberUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(GuildInformationsPaddocksMessage(), True, True)
        StoreDataManager().registerClass(GuildMemberLeavingMessage(), True, True)
        StoreDataManager().registerClass(GuildLeftMessage(), True, True)
        StoreDataManager().registerClass(GuildMembershipMessage(), True, True)
        StoreDataManager().registerClass(GuildLevelUpMessage(), True, True)
        StoreDataManager().registerClass(GuildInfosUpgradeMessage(), True, True)
        StoreDataManager().registerClass(GuildHousesInformationMessage(), True, True)
        StoreDataManager().registerClass(
            GuildHouseUpdateInformationMessage(), True, True
        )
        StoreDataManager().registerClass(GuildHouseRemoveMessage(), True, True)
        StoreDataManager().registerClass(GuildPaddockBoughtMessage(), True, True)
        StoreDataManager().registerClass(GuildPaddockRemovedMessage(), True, True)
        StoreDataManager().registerClass(
            GuildMemberWarnOnConnectionStateMessage(), True, True
        )
        StoreDataManager().registerClass(GuildMotdMessage(), True, True)
        StoreDataManager().registerClass(GuildMotdSetErrorMessage(), True, True)
        StoreDataManager().registerClass(GuildBulletinMessage(), True, True)
        StoreDataManager().registerClass(GuildBulletinSetErrorMessage(), True, True)
        StoreDataManager().registerClass(GuildFactsErrorMessage(), True, True)
        StoreDataManager().registerClass(GuildFactsMessage(), True, True)
        StoreDataManager().registerClass(GuildInAllianceFactsMessage(), True, True)
        StoreDataManager().registerClass(GuildRanksMessage(), True, True)
        StoreDataManager().registerClass(AllianceFactsErrorMessage(), True, True)
        StoreDataManager().registerClass(AllianceFactsMessage(), True, True)
        StoreDataManager().registerClass(GuildListMessage(), True, True)
        StoreDataManager().registerClass(GuildVersatileInfoListMessage(), True, True)
        StoreDataManager().registerClass(AllianceListMessage(), True, True)
        StoreDataManager().registerClass(AlliancePartialListMessage(), True, True)
        StoreDataManager().registerClass(AllianceInsiderInfoMessage(), True, True)
        StoreDataManager().registerClass(AllianceMotdMessage(), True, True)
        StoreDataManager().registerClass(AllianceMotdSetErrorMessage(), True, True)
        StoreDataManager().registerClass(AllianceBulletinMessage(), True, True)
        StoreDataManager().registerClass(AllianceBulletinSetErrorMessage(), True, True)
        StoreDataManager().registerClass(TaxCollectorMovementMessage(), True, True)
        StoreDataManager().registerClass(TaxCollectorErrorMessage(), True, True)
        StoreDataManager().registerClass(AbstractTaxCollectorListMessage(), True, True)
        StoreDataManager().registerClass(TaxCollectorListMessage(), True, True)
        StoreDataManager().registerClass(TopTaxCollectorListMessage(), True, True)
        StoreDataManager().registerClass(TaxCollectorStateUpdateMessage(), True, True)
        StoreDataManager().registerClass(TaxCollectorMovementAddMessage(), True, True)
        StoreDataManager().registerClass(
            TaxCollectorMovementRemoveMessage(), True, True
        )
        StoreDataManager().registerClass(TaxCollectorAttackedMessage(), True, True)
        StoreDataManager().registerClass(
            TaxCollectorAttackedResultMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildFightPlayersHelpersJoinMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildFightPlayersHelpersLeaveMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildFightPlayersEnemiesListMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildFightPlayersEnemyRemoveMessage(), True, True
        )
        StoreDataManager().registerClass(
            TaxCollectorMovementsOfflineMessage(), True, True
        )
        StoreDataManager().registerClass(RecruitmentInformationMessage(), True, True)
        StoreDataManager().registerClass(
            GuildRecruitmentInvalidateMessage(), True, True
        )
        StoreDataManager().registerClass(GuildApplicationDeletedMessage(), True, True)
        StoreDataManager().registerClass(
            GuildPlayerApplicationAbstractMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildPlayerApplicationInformationMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildPlayerNoApplicationInformationMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildApplicationIsAnsweredMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildListApplicationAnswerMessage(), True, True
        )
        StoreDataManager().registerClass(
            GuildListApplicationModifiedMessage(), True, True
        )
        StoreDataManager().registerClass(GuildApplicationReceivedMessage(), True, True)
        StoreDataManager().registerClass(
            ListenersOfSynchronizedStorageMessage(), True, True
        )
        StoreDataManager().registerClass(
            AddListenerOnSynchronizedStorageMessage(), True, True
        )
        StoreDataManager().registerClass(
            RemoveListenerOnSynchronizedStorageMessage(), True, True
        )
        StoreDataManager().registerClass(PrismSetSabotagedRefusedMessage(), True, True)
        StoreDataManager().registerClass(PrismFightDefenderAddMessage(), True, True)
        StoreDataManager().registerClass(PrismFightDefenderLeaveMessage(), True, True)
        StoreDataManager().registerClass(PrismFightAttackerAddMessage(), True, True)
        StoreDataManager().registerClass(PrismFightAttackerRemoveMessage(), True, True)
        StoreDataManager().registerClass(PrismsListMessage(), True, True)
        StoreDataManager().registerClass(PrismsListUpdateMessage(), True, True)
        StoreDataManager().registerClass(ChallengeFightJoinRefusedMessage(), True, True)
        StoreDataManager().registerClass(PrismInfoCloseMessage(), True, True)
        StoreDataManager().registerClass(PrismsInfoValidMessage(), True, True)
        StoreDataManager().registerClass(PrismFightAddedMessage(), True, True)
        StoreDataManager().registerClass(PrismFightRemovedMessage(), True, True)
        StoreDataManager().registerClass(PrismInfoInValidMessage(), True, True)
        StoreDataManager().registerClass(PrismFightStateUpdateMessage(), True, True)
        StoreDataManager().registerClass(PrismSettingsErrorMessage(), True, True)
        StoreDataManager().registerClass(QuestListMessage(), True, True)
        StoreDataManager().registerClass(QuestStartedMessage(), True, True)
        StoreDataManager().registerClass(QuestValidatedMessage(), True, True)
        StoreDataManager().registerClass(QuestObjectiveValidatedMessage(), True, True)
        StoreDataManager().registerClass(QuestStepValidatedMessage(), True, True)
        StoreDataManager().registerClass(QuestStepStartedMessage(), True, True)
        StoreDataManager().registerClass(QuestStepInfoMessage(), True, True)
        StoreDataManager().registerClass(FollowedQuestsMessage(), True, True)
        StoreDataManager().registerClass(WatchQuestStepInfoMessage(), True, True)
        StoreDataManager().registerClass(WatchQuestListMessage(), True, True)
        StoreDataManager().registerClass(NotificationListMessage(), True, True)
        StoreDataManager().registerClass(NotificationByServerMessage(), True, True)
        StoreDataManager().registerClass(SubscriptionLimitationMessage(), True, True)
        StoreDataManager().registerClass(SubscriptionZoneMessage(), True, True)
        StoreDataManager().registerClass(GuestLimitationMessage(), True, True)
        StoreDataManager().registerClass(GuestModeMessage(), True, True)
        StoreDataManager().registerClass(
            ListMapNpcsQuestStatusUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(NpcGenericActionFailureMessage(), True, True)
        StoreDataManager().registerClass(PortalDialogCreationMessage(), True, True)
        StoreDataManager().registerClass(NpcDialogCreationMessage(), True, True)
        StoreDataManager().registerClass(NpcDialogQuestionMessage(), True, True)
        StoreDataManager().registerClass(
            TaxCollectorDialogQuestionBasicMessage(), True, True
        )
        StoreDataManager().registerClass(
            TaxCollectorDialogQuestionExtendedMessage(), True, True
        )
        StoreDataManager().registerClass(
            AllianceTaxCollectorDialogQuestionExtendedMessage(), True, True
        )
        StoreDataManager().registerClass(
            AlliancePrismDialogQuestionMessage(), True, True
        )
        StoreDataManager().registerClass(EntityTalkMessage(), True, True)
        StoreDataManager().registerClass(JobDescriptionMessage(), True, True)
        StoreDataManager().registerClass(JobLevelUpMessage(), True, True)
        StoreDataManager().registerClass(JobExperienceMultiUpdateMessage(), True, True)
        StoreDataManager().registerClass(JobExperienceUpdateMessage(), True, True)
        StoreDataManager().registerClass(
            JobExperienceOtherPlayerUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(JobAllowMultiCraftRequestMessage(), True, True)
        StoreDataManager().registerClass(
            JobMultiCraftAvailableSkillsMessage(), True, True
        )
        StoreDataManager().registerClass(JobCrafterDirectoryListMessage(), True, True)
        StoreDataManager().registerClass(
            JobCrafterDirectorySettingsMessage(), True, True
        )
        StoreDataManager().registerClass(JobBookSubscriptionMessage(), True, True)
        StoreDataManager().registerClass(JobCrafterDirectoryRemoveMessage(), True, True)
        StoreDataManager().registerClass(JobCrafterDirectoryAddMessage(), True, True)
        StoreDataManager().registerClass(JobCrafterDirectoryEntryMessage(), True, True)
        StoreDataManager().registerClass(KamasUpdateMessage(), True, True)
        StoreDataManager().registerClass(ObjectGroundAddedMessage(), True, True)
        StoreDataManager().registerClass(ObjectGroundListAddedMessage(), True, True)
        StoreDataManager().registerClass(ObjectGroundRemovedMessage(), True, True)
        StoreDataManager().registerClass(
            ObjectGroundRemovedMultipleMessage(), True, True
        )
        StoreDataManager().registerClass(InventoryContentMessage(), True, True)
        StoreDataManager().registerClass(WatchInventoryContentMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarContentMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarAddErrorMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarRemoveErrorMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarSwapErrorMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarRefreshMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarRemovedMessage(), True, True)
        StoreDataManager().registerClass(ShortcutBarReplacedMessage(), True, True)
        StoreDataManager().registerClass(StorageInventoryContentMessage(), True, True)
        StoreDataManager().registerClass(StorageKamasUpdateMessage(), True, True)
        StoreDataManager().registerClass(StorageObjectUpdateMessage(), True, True)
        StoreDataManager().registerClass(StorageObjectsUpdateMessage(), True, True)
        StoreDataManager().registerClass(StorageObjectRemoveMessage(), True, True)
        StoreDataManager().registerClass(StorageObjectsRemoveMessage(), True, True)
        StoreDataManager().registerClass(SetUpdateMessage(), True, True)
        StoreDataManager().registerClass(InventoryWeightMessage(), True, True)
        StoreDataManager().registerClass(ObjectMovementMessage(), True, True)
        StoreDataManager().registerClass(ObjectAddedMessage(), True, True)
        StoreDataManager().registerClass(ObjectsAddedMessage(), True, True)
        StoreDataManager().registerClass(GoldAddedMessage(), True, True)
        StoreDataManager().registerClass(ObjectErrorMessage(), True, True)
        StoreDataManager().registerClass(ObjectDeletedMessage(), True, True)
        StoreDataManager().registerClass(ObjectsDeletedMessage(), True, True)
        StoreDataManager().registerClass(ObjectQuantityMessage(), True, True)
        StoreDataManager().registerClass(ObjectsQuantityMessage(), True, True)
        StoreDataManager().registerClass(ObjectModifiedMessage(), True, True)
        StoreDataManager().registerClass(ObjectJobAddedMessage(), True, True)
        StoreDataManager().registerClass(ObtainedItemMessage(), True, True)
        StoreDataManager().registerClass(ObtainedItemWithBonusMessage(), True, True)
        StoreDataManager().registerClass(LivingObjectMessageMessage(), True, True)
        StoreDataManager().registerClass(SymbioticObjectErrorMessage(), True, True)
        StoreDataManager().registerClass(SymbioticObjectAssociatedMessage(), True, True)
        StoreDataManager().registerClass(WrapperObjectErrorMessage(), True, True)
        StoreDataManager().registerClass(WrapperObjectAssociatedMessage(), True, True)
        StoreDataManager().registerClass(MimicryObjectPreviewMessage(), True, True)
        StoreDataManager().registerClass(MimicryObjectErrorMessage(), True, True)
        StoreDataManager().registerClass(MimicryObjectAssociatedMessage(), True, True)
        StoreDataManager().registerClass(InvalidPresetsMessage(), True, True)
        StoreDataManager().registerClass(PresetsMessage(), True, True)
        StoreDataManager().registerClass(ItemForPresetUpdateMessage(), True, True)
        StoreDataManager().registerClass(PresetSavedMessage(), True, True)
        StoreDataManager().registerClass(PresetSaveErrorMessage(), True, True)
        StoreDataManager().registerClass(PresetDeleteResultMessage(), True, True)
        StoreDataManager().registerClass(PresetUseResultMessage(), True, True)
        StoreDataManager().registerClass(
            PresetUseResultWithMissingIdsMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeMoneyMovementInformationMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeCraftCountModifiedMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeObjectMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectAddedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectsAddedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectRemovedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectsRemovedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectModifiedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectsModifiedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeObjectPutInBagMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeObjectRemovedFromBagMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeObjectModifiedInBagMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeKamaModifiedMessage(), True, True)
        StoreDataManager().registerClass(ExchangePodsModifiedMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeRequestedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeRequestedTradeMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStartedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStartedWithPodsMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeStartedWithStorageMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeBidHouseBuyResultMessage(), True, True)
        StoreDataManager().registerClass(ExchangeBidHouseItemAddOkMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeBidHouseItemRemoveOkMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeBidHouseGenericItemAddedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeBidHouseGenericItemRemovedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeBidHouseInListAddedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeBidHouseInListUpdatedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeBidHouseInListRemovedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeBidHouseUnsoldItemsMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeOfflineSoldItemsMessage(), True, True)
        StoreDataManager().registerClass(ExchangeIsReadyMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStoppedMessage(), True, True)
        StoreDataManager().registerClass(ExchangeErrorMessage(), True, True)
        StoreDataManager().registerClass(ExchangeLeaveMessage(), True, True)
        StoreDataManager().registerClass(DecraftResultMessage(), True, True)
        StoreDataManager().registerClass(RecycleResultMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStartOkNpcTradeMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStartOkRunesTradeMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeStartOkEvolutiveObjectRecycleTradeMessage(), True, True
        )
        StoreDataManager().registerClass(
            EvolutiveObjectRecycleResultMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeStartOkRecycleTradeMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeStartOkNpcShopMessage(), True, True)
        StoreDataManager().registerClass(ExchangeOkMultiCraftMessage(), True, True)
        StoreDataManager().registerClass(ExchangeCraftResultMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeCraftResultWithObjectIdMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeCraftResultWithObjectDescMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeCraftResultMagicWithObjectDescMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeStartOkHumanVendorMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeShopStockStartedMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeShopStockMovementUpdatedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeShopStockMultiMovementUpdatedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeShopStockMovementRemovedMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeShopStockMultiMovementRemovedMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeStartedMountStockMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeStartedTaxCollectorShopMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeStartedBidSellerMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStartedBidBuyerMessage(), True, True)
        StoreDataManager().registerClass(ExchangeBidPriceMessage(), True, True)
        StoreDataManager().registerClass(ExchangeBidPriceForSellerMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeTypesExchangerDescriptionForUserMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeTypesItemsExchangerDescriptionForUserMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeWeightMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeGuildTaxCollectorGetMessage(), True, True
        )
        StoreDataManager().registerClass(ItemNoMoreAvailableMessage(), True, True)
        StoreDataManager().registerClass(ExchangeBuyOkMessage(), True, True)
        StoreDataManager().registerClass(ExchangeSellOkMessage(), True, True)
        StoreDataManager().registerClass(ExchangeReplyTaxVendorMessage(), True, True)
        StoreDataManager().registerClass(ExchangeWaitingResultMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeStartOkMountWithOutPaddockMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeStartOkMountMessage(), True, True)
        StoreDataManager().registerClass(ExchangeMountStableErrorMessage(), True, True)
        StoreDataManager().registerClass(ExchangeMountsStableAddMessage(), True, True)
        StoreDataManager().registerClass(ExchangeMountsPaddockAddMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeMountsStableBornAddMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeMountsStableRemoveMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeMountsPaddockRemoveMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeMountsTakenFromPaddockMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeMountFreeFromPaddockMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeMountSterilizeFromPaddockMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeBidSearchOkMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeItemAutoCraftStopedMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeStartOkCraftMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeStartOkCraftWithInformationMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeStartOkMulticraftCrafterMessage(), True, True
        )
        StoreDataManager().registerClass(
            ExchangeStartOkMulticraftCustomerMessage(), True, True
        )
        StoreDataManager().registerClass(ExchangeCrafterJobLevelupMessage(), True, True)
        StoreDataManager().registerClass(ExchangeStartOkJobIndexMessage(), True, True)
        StoreDataManager().registerClass(
            ExchangeCraftPaymentModifiedMessage(), True, True
        )
        StoreDataManager().registerClass(
            UpdateMountCharacteristicsMessage(), True, True
        )
        StoreDataManager().registerClass(ObjectAveragePricesErrorMessage(), True, True)
        StoreDataManager().registerClass(ObjectAveragePricesMessage(), True, True)
        StoreDataManager().registerClass(PurchasableDialogMessage(), True, True)
        StoreDataManager().registerClass(AccountHouseMessage(), True, True)
        StoreDataManager().registerClass(HousePropertiesMessage(), True, True)
        StoreDataManager().registerClass(HouseBuyResultMessage(), True, True)
        StoreDataManager().registerClass(HouseSellingUpdateMessage(), True, True)
        StoreDataManager().registerClass(HouseToSellListMessage(), True, True)
        StoreDataManager().registerClass(HouseGuildNoneMessage(), True, True)
        StoreDataManager().registerClass(HouseGuildRightsMessage(), True, True)
        StoreDataManager().registerClass(PaddockBuyResultMessage(), True, True)
        StoreDataManager().registerClass(PaddockPropertiesMessage(), True, True)
        StoreDataManager().registerClass(PaddockSellBuyDialogMessage(), True, True)
        StoreDataManager().registerClass(
            GameDataPlayFarmObjectAnimationMessage(), True, True
        )
        StoreDataManager().registerClass(PaddockToSellListMessage(), True, True)
        StoreDataManager().registerClass(HavenBagRoomUpdateMessage(), True, True)
        StoreDataManager().registerClass(HavenBagPackListMessage(), True, True)
        StoreDataManager().registerClass(EditHavenBagStartMessage(), True, True)
        StoreDataManager().registerClass(EditHavenBagFinishedMessage(), True, True)
        StoreDataManager().registerClass(HavenBagDailyLoteryMessage(), True, True)
        StoreDataManager().registerClass(HavenBagFurnituresMessage(), True, True)
        StoreDataManager().registerClass(
            MapComplementaryInformationsDataInHavenBagMessage(), True, True
        )
        StoreDataManager().registerClass(HavenBagPermissionsUpdateMessage(), True, True)
        StoreDataManager().registerClass(InviteInHavenBagClosedMessage(), True, True)
        StoreDataManager().registerClass(InviteInHavenBagMessage(), True, True)
        StoreDataManager().registerClass(InviteInHavenBagOfferMessage(), True, True)
        StoreDataManager().registerClass(MountSterilizedMessage(), True, True)
        StoreDataManager().registerClass(MountReleasedMessage(), True, True)
        StoreDataManager().registerClass(MountRenamedMessage(), True, True)
        StoreDataManager().registerClass(MountXpRatioMessage(), True, True)
        StoreDataManager().registerClass(MountDataMessage(), True, True)
        StoreDataManager().registerClass(MountDataErrorMessage(), True, True)
        StoreDataManager().registerClass(MountSetMessage(), True, True)
        StoreDataManager().registerClass(MountUnSetMessage(), True, True)
        StoreDataManager().registerClass(MountEquipedErrorMessage(), True, True)
        StoreDataManager().registerClass(MountRidingMessage(), True, True)
        StoreDataManager().registerClass(
            GameDataPaddockObjectRemoveMessage(), True, True
        )
        StoreDataManager().registerClass(GameDataPaddockObjectAddMessage(), True, True)
        StoreDataManager().registerClass(
            GameDataPaddockObjectListAddMessage(), True, True
        )
        StoreDataManager().registerClass(MountEmoteIconUsedOkMessage(), True, True)
        StoreDataManager().registerClass(LockableShowCodeDialogMessage(), True, True)
        StoreDataManager().registerClass(LockableCodeResultMessage(), True, True)
        StoreDataManager().registerClass(
            LockableStateUpdateAbstractMessage(), True, True
        )
        StoreDataManager().registerClass(
            LockableStateUpdateHouseDoorMessage(), True, True
        )
        StoreDataManager().registerClass(
            LockableStateUpdateStorageMessage(), True, True
        )
        StoreDataManager().registerClass(DocumentReadingBeginMessage(), True, True)
        StoreDataManager().registerClass(TitlesAndOrnamentsListMessage(), True, True)
        StoreDataManager().registerClass(TitleGainedMessage(), True, True)
        StoreDataManager().registerClass(TitleLostMessage(), True, True)
        StoreDataManager().registerClass(OrnamentGainedMessage(), True, True)
        StoreDataManager().registerClass(OrnamentLostMessage(), True, True)
        StoreDataManager().registerClass(TitleSelectedMessage(), True, True)
        StoreDataManager().registerClass(TitleSelectErrorMessage(), True, True)
        StoreDataManager().registerClass(OrnamentSelectedMessage(), True, True)
        StoreDataManager().registerClass(OrnamentSelectErrorMessage(), True, True)
        StoreDataManager().registerClass(ContactLookMessage(), True, True)
        StoreDataManager().registerClass(ContactLookErrorMessage(), True, True)
        StoreDataManager().registerClass(SocialNoticeMessage(), True, True)
        StoreDataManager().registerClass(BulletinMessage(), True, True)
        StoreDataManager().registerClass(SocialNoticeSetErrorMessage(), True, True)
        StoreDataManager().registerClass(AccessoryPreviewErrorMessage(), True, True)
        StoreDataManager().registerClass(AccessoryPreviewMessage(), True, True)
        StoreDataManager().registerClass(HaapiBufferListMessage(), True, True)
        StoreDataManager().registerClass(HaapiConfirmationMessage(), True, True)
        StoreDataManager().registerClass(HaapiValidationMessage(), True, True)
        StoreDataManager().registerClass(HaapiBuyValidationMessage(), True, True)
        StoreDataManager().registerClass(HaapiApiKeyMessage(), True, True)
        StoreDataManager().registerClass(HaapiShopApiKeyMessage(), True, True)
        StoreDataManager().registerClass(FinishMoveListMessage(), True, True)
        StoreDataManager().registerClass(
            TreasureHuntShowLegendaryUIMessage(), True, True
        )
        StoreDataManager().registerClass(TreasureHuntRequestAnswerMessage(), True, True)
        StoreDataManager().registerClass(TreasureHuntMessage(), True, True)
        StoreDataManager().registerClass(TreasureHuntFinishedMessage(), True, True)
        StoreDataManager().registerClass(
            TreasureHuntDigRequestAnswerMessage(), True, True
        )
        StoreDataManager().registerClass(
            TreasureHuntDigRequestAnswerFailedMessage(), True, True
        )
        StoreDataManager().registerClass(
            TreasureHuntFlagRequestAnswerMessage(), True, True
        )
        StoreDataManager().registerClass(
            TreasureHuntAvailableRetryCountUpdateMessage(), True, True
        )
        StoreDataManager().registerClass(BreachStateMessage(), True, True)
        StoreDataManager().registerClass(BreachCharactersMessage(), True, True)
        StoreDataManager().registerClass(BreachBonusMessage(), True, True)
        StoreDataManager().registerClass(BreachBudgetMessage(), True, True)
        StoreDataManager().registerClass(BreachSavedMessage(), True, True)
        StoreDataManager().registerClass(BreachBranchesMessage(), True, True)
        StoreDataManager().registerClass(BreachRewardsMessage(), True, True)
        StoreDataManager().registerClass(BreachRewardBoughtMessage(), True, True)
        StoreDataManager().registerClass(BreachInvitationOfferMessage(), True, True)
        StoreDataManager().registerClass(BreachInvitationResponseMessage(), True, True)
        StoreDataManager().registerClass(BreachInvitationCloseMessage(), True, True)
        StoreDataManager().registerClass(BreachKickResponseMessage(), True, True)
        StoreDataManager().registerClass(
            AnomalySubareaInformationResponseMessage(), True, True
        )
        StoreDataManager().registerClass(
            AlignmentWarEffortProgressionMessage(), True, True
        )
        StoreDataManager().registerClass(
            CharacterAlignmentWarEffortProgressionMessage(), True, True
        )
        StoreDataManager().registerClass(
            AlignmentWarEffortDonatePreviewMessage(), True, True
        )
        StoreDataManager().registerClass(
            AlignmentWarEffortDonationResultMessage(), True, True
        )
        StoreDataManager().registerClass(HaapiTokenMessage(), True, True)
        StoreDataManager().registerClass(HaapiAuthErrorMessage(), True, True)
        StoreDataManager().registerClass(HaapiSessionMessage(), True, True)
        StoreDataManager().registerClass(DebtsUpdateMessage(), True, True)
        StoreDataManager().registerClass(DebtsDeleteMessage(), True, True)
        StoreDataManager().registerClass(ActivitySuggestionsMessage(), True, True)
